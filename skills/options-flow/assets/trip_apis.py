#!/usr/bin/env python3
"""trip_apis — standalone domain data for the `trip` profile of /options.

Port of an internal `personal_apis.py` with internal deps removed
(`.config`/`.errors`/`.security`). Self-contained: stdlib + requests only.
3 of 4 sources need NO key (Nominatim geocode, Open-Meteo weather,
sunrise-sunset.org). eBird needs a free key via EBIRD_API_KEY env var;
without it, eBird calls degrade gracefully (empty result + a note) so the
caller can fall back to WebSearch.

CLI (so the flow can call it over Bash):
  python3 trip_apis.py geocode "Málaga, Spain"
  python3 trip_apis.py gps 36.675 -4.499            # decimal + DMS + maps link
  python3 trip_apis.py weather 36.675 -4.499 --days 7
  python3 trip_apis.py sun 36.675 -4.499 [--date 2026-12-19]
  python3 trip_apis.py hotspots 37.13 -6.49 --dist 30 --max 10   # needs EBIRD_API_KEY
  python3 trip_apis.py distance 36.675 -4.499 37.13 -6.49

All commands print JSON to stdout. On failure they print {"error": "..."} and exit 1.
"""
from __future__ import annotations

import argparse
import functools
import json
import math
import os
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional

try:
    import requests
except ImportError:  # pragma: no cover
    sys.stderr.write("trip_apis needs `requests` (pip install requests)\n")
    raise

USER_AGENT = "deep-research-options-flow/1.0 (trip profile)"

# Module-level courtesy pacers for keyless public APIs called in batches
# (Nominatim usage policy mandates <=1 req/s; sunrise-sunset.org throttles bursts).
_NOMINATIM_PACE = 1.1   # seconds between geocode calls
_SUN_PACE = 0.4         # seconds between sun-times calls
_last_call: Dict[str, float] = {}


def _pace(key: str, interval: float) -> None:
    dt = time.time() - _last_call.get(key, 0.0)
    if dt < interval:
        time.sleep(interval - dt)
    _last_call[key] = time.time()


class TripAPIError(Exception):
    """Error in trip API operations."""


def safe(fallback: Any):
    """Decorator: on any exception return `fallback` (graceful degrade)."""
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            try:
                return fn(*a, **kw)
            except Exception as e:  # noqa: BLE001 — intentional broad degrade
                sys.stderr.write(f"[trip_apis] {fn.__name__}: {e}\n")
                return fallback
        return wrapper
    return deco


class _RateLimiter:
    """Minimal inline rate limiter (per-minute), simple per-minute limiter."""

    def __init__(self, calls_per_minute: int = 10):
        self.min_interval = 60.0 / max(1, calls_per_minute)
        self._last = 0.0

    def wait(self) -> None:
        dt = time.time() - self._last
        if dt < self.min_interval:
            time.sleep(self.min_interval - dt)
        self._last = time.time()


# ============================================================================
# Data Models
# ============================================================================

@dataclass
class Location:
    name: str
    latitude: float
    longitude: float
    description: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class BirdingHotspot:
    loc_id: str
    loc_name: str
    latitude: float
    longitude: float
    country_code: str
    subnational1_code: str
    latest_obs_dt: Optional[str] = None
    num_species_all_time: Optional[int] = None
    distance_km: Optional[float] = None

    def to_dict(self) -> Dict:
        return asdict(self)


# ============================================================================
# Geolocation
# ============================================================================

class GeoUtils:
    @staticmethod
    def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Distance between two points (km), Haversine."""
        R = 6371
        p1, p2 = math.radians(lat1), math.radians(lat2)
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlon / 2) ** 2
        return R * 2 * math.asin(math.sqrt(a))

    @staticmethod
    def format_gps(latitude: float, longitude: float) -> Dict[str, str]:
        """Return decimal, DMS, and a Google Maps link for one point."""
        def to_dms(dec: float, is_lat: bool) -> str:
            direction = ("N" if dec >= 0 else "S") if is_lat else ("E" if dec >= 0 else "W")
            dec = abs(dec)
            deg = int(dec)
            mdec = (dec - deg) * 60
            minutes = int(mdec)
            sec = (mdec - minutes) * 60
            return f"{deg}°{minutes}'{sec:.1f}\"{direction}"

        return {
            "decimal": f"{latitude:.6f}, {longitude:.6f}",
            "dms": f"{to_dms(latitude, True)}, {to_dms(longitude, False)}",
            "google_maps": f"https://www.google.com/maps?q={latitude},{longitude}",
        }

    @staticmethod
    @safe(fallback=None)
    def geocode(location_name: str) -> Optional[Location]:
        """Geocode a name → Location via OpenStreetMap Nominatim (no key)."""
        _pace("nominatim", _NOMINATIM_PACE)
        resp = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": location_name, "format": "json", "limit": 1},
            headers={"User-Agent": USER_AGENT},
            timeout=10,
        )
        resp.raise_for_status()
        results = resp.json()
        if not results:
            return None
        r = results[0]
        return Location(
            name=r.get("display_name", location_name),
            latitude=float(r["lat"]),
            longitude=float(r["lon"]),
            description=f"Geocoded from: {location_name}",
        )


# ============================================================================
# eBird (needs free key; degrades to [] without one)
# ============================================================================

class EBirdAPI:
    BASE_URL = "https://api.ebird.org/v2"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("EBIRD_API_KEY")
        self.rate = _RateLimiter(calls_per_minute=10)

    @property
    def available(self) -> bool:
        return bool(self.api_key)

    def _get(self, endpoint: str, params: Dict) -> Any:
        if not self.api_key:
            raise TripAPIError("EBIRD_API_KEY not set — eBird unavailable (use WebSearch fallback)")
        self.rate.wait()
        resp = requests.get(
            f"{self.BASE_URL}/{endpoint}",
            headers={"X-eBirdApiToken": self.api_key},
            params=params,
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()

    @safe(fallback=[])
    def find_nearby_hotspots(self, latitude: float, longitude: float,
                             max_distance_km: int = 50, max_results: int = 10) -> List[Dict]:
        data = self._get("ref/hotspot/geo",
                         {"lat": latitude, "lng": longitude, "dist": max_distance_km, "fmt": "json"})
        spots = []
        for item in data[:max_results]:
            d = GeoUtils.haversine_distance(latitude, longitude, item["lat"], item["lng"])
            spots.append(BirdingHotspot(
                loc_id=item["locId"], loc_name=item["locName"],
                latitude=item["lat"], longitude=item["lng"],
                country_code=item.get("countryCode", ""),
                subnational1_code=item.get("subnational1Code", ""),
                latest_obs_dt=item.get("latestObsDt"),
                num_species_all_time=item.get("numSpeciesAllTime"),
                distance_km=round(d, 2),
            ).to_dict())
        spots.sort(key=lambda x: x["distance_km"])
        return spots

    @safe(fallback=[])
    def get_recent_observations(self, location_id: str, days_back: int = 14,
                                max_results: int = 50) -> List[Dict]:
        return self._get(f"data/obs/{location_id}/recent",
                         {"back": days_back, "maxResults": max_results})

    @safe(fallback=[])
    def get_notable_observations(self, latitude: float, longitude: float,
                                 max_distance_km: int = 50, days_back: int = 14) -> List[Dict]:
        return self._get("data/obs/geo/recent/notable",
                         {"lat": latitude, "lng": longitude, "dist": max_distance_km, "back": days_back})


# ============================================================================
# Weather (Open-Meteo, no key)
# ============================================================================

class WeatherAPI:
    BASE_URL = "https://api.open-meteo.com/v1"

    _WMO = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow", 77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm w/ slight hail", 99: "Thunderstorm w/ heavy hail",
    }

    @classmethod
    def interpret_code(cls, code: int) -> str:
        return cls._WMO.get(code, f"Unknown ({code})")

    @safe(fallback=None)
    def get_forecast(self, latitude: float, longitude: float, days: int = 7) -> Optional[Dict]:
        resp = requests.get(
            f"{self.BASE_URL}/forecast",
            params={
                "latitude": latitude, "longitude": longitude,
                "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,"
                         "precipitation_probability_max,windspeed_10m_max,cloudcover_mean,weathercode",
                "timezone": "auto", "forecast_days": days,
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        # annotate weather codes with text for readability
        daily = data.get("daily", {})
        codes = daily.get("weathercode", [])
        daily["weather_text"] = [self.interpret_code(c) for c in codes]
        return data


# ============================================================================
# Sun times (sunrise-sunset.org, no key) → golden/blue hours
# ============================================================================

class SunTimesAPI:
    BASE_URL = "https://api.sunrise-sunset.org/json"

    @safe(fallback=None)
    def get_sun_times(self, latitude: float, longitude: float,
                      date: Optional[str] = None) -> Optional[Dict]:
        params = {"lat": latitude, "lng": longitude, "formatted": 0}
        if date:
            params["date"] = date
        _pace("sun", _SUN_PACE)
        resp = requests.get(self.BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") == "OK":
            r = data["results"]
            # surface the photographer-relevant fields explicitly
            return {
                "sunrise": r.get("sunrise"),
                "sunset": r.get("sunset"),
                "golden_hour_morning_until": r.get("sunrise"),  # ~sunrise → +1h
                "golden_hour_evening_from": r.get("sunset"),    # ~ -1h → sunset
                "civil_twilight_begin": r.get("civil_twilight_begin"),  # blue hour am
                "civil_twilight_end": r.get("civil_twilight_end"),      # blue hour pm
                "day_length_s": r.get("day_length"),
                "raw": r,
            }
        return None


# ============================================================================
# CLI
# ============================================================================

def _out(obj: Any) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2, default=str))


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="trip_apis — domain data for /options trip profile")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("geocode"); g.add_argument("name")
    gp = sub.add_parser("gps"); gp.add_argument("lat", type=float); gp.add_argument("lng", type=float)
    w = sub.add_parser("weather"); w.add_argument("lat", type=float); w.add_argument("lng", type=float); w.add_argument("--days", type=int, default=7)
    s = sub.add_parser("sun"); s.add_argument("lat", type=float); s.add_argument("lng", type=float); s.add_argument("--date", default=None)
    h = sub.add_parser("hotspots"); h.add_argument("lat", type=float); h.add_argument("lng", type=float); h.add_argument("--dist", type=int, default=50); h.add_argument("--max", type=int, default=10)
    d = sub.add_parser("distance"); d.add_argument("lat1", type=float); d.add_argument("lng1", type=float); d.add_argument("lat2", type=float); d.add_argument("lng2", type=float)

    args = p.parse_args(argv)

    if args.cmd == "geocode":
        loc = GeoUtils.geocode(args.name)
        if not loc:
            _out({"error": f"could not geocode: {args.name}"}); return 1
        out = loc.to_dict(); out["gps"] = GeoUtils.format_gps(loc.latitude, loc.longitude); _out(out); return 0

    if args.cmd == "gps":
        _out(GeoUtils.format_gps(args.lat, args.lng)); return 0

    if args.cmd == "distance":
        km = GeoUtils.haversine_distance(args.lat1, args.lng1, args.lat2, args.lng2)
        _out({"distance_km": round(km, 2)}); return 0

    if args.cmd == "weather":
        data = WeatherAPI().get_forecast(args.lat, args.lng, days=args.days)
        if data is None:
            _out({"error": "weather fetch failed"}); return 1
        _out(data); return 0

    if args.cmd == "sun":
        data = SunTimesAPI().get_sun_times(args.lat, args.lng, date=args.date)
        if data is None:
            _out({"error": "sun times fetch failed"}); return 1
        _out(data); return 0

    if args.cmd == "hotspots":
        api = EBirdAPI()
        if not api.available:
            _out({"error": "EBIRD_API_KEY not set", "fallback": "use WebSearch for eBird hotspots", "hotspots": []}); return 1
        _out({"hotspots": api.find_nearby_hotspots(args.lat, args.lng, max_distance_km=args.dist, max_results=args.max)}); return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
