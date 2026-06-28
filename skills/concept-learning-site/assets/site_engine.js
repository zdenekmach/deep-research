/* site_engine.js — datově řízené mapy a galerie pro concept-learning-site.
 * Čte JSON z <script id="site-data">, vykreslí do placeholderů:
 *   <div class="cls-map" data-map="ID"></div>
 *   <div class="cls-gallery" data-gallery="ID"></div>
 * Kontrakt: docs/SPEC-site-engine.md. Bez dat / bez placeholderů je no-op.
 */
(function () {
  var el = document.getElementById('site-data');
  var DATA = {};
  try { DATA = JSON.parse(el ? el.textContent : '{}') || {}; }
  catch (e) { console.error('[site_engine] site-data parse error', e); }

  var CAT = DATA.categories || {};
  var POINTS = DATA.points || [];
  var MAPS = DATA.maps || {};
  var GALLERIES = DATA.galleries || {};

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function attr(s) { return esc(s).replace(/"/g, '&quot;'); }

  function legend(map, spec) {
    if (typeof L === 'undefined') return;
    var lg = L.control({ position: 'bottomright' });
    lg.onAdd = function () {
      var d = L.DomUtil.create('div', 'maplegend'), h = '';
      Object.keys(CAT).forEach(function (k) {
        h += '<i style="background:' + CAT[k].color + '"></i>' + esc(CAT[k].label) + '<br>';
      });
      if (spec.route && spec.route.length) {
        var col = spec.routeColor || '#4a90d9';
        h += '<span style="border-top:2px dashed ' + col +
             ';display:inline-block;width:16px;margin-right:6px;vertical-align:middle"></span>trasa';
      }
      d.innerHTML = h; return d;
    };
    lg.addTo(map);
  }

  function renderMap(node) {
    if (typeof L === 'undefined') { console.warn('[site_engine] Leaflet missing'); return; }
    var id = node.getAttribute('data-map');
    var spec = MAPS[id];
    if (!spec) { node.style.display = 'none'; return; }

    var map = L.map(node, { scrollWheelZoom: false });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      { maxZoom: 18, attribution: '© OpenStreetMap' }).addTo(map);

    var bounds = [];
    var tag = spec.filterTag;
    POINTS.filter(function (p) { return !tag || (p.tags || []).indexOf(tag) >= 0; })
      .forEach(function (p) {
        var c = (CAT[p.cat] || {}).color || '#4a90d9';
        L.circleMarker([p.lat, p.lng], {
          radius: 7, color: '#0b0e12', weight: 1.5, fillColor: c, fillOpacity: .95
        }).bindPopup('<b>' + esc(p.name) + '</b>' + (p.desc ? '<br>' + esc(p.desc) : ''))
          .addTo(map);
        bounds.push([p.lat, p.lng]);
      });

    if (spec.route && spec.route.length) {
      var col = spec.routeColor || '#4a90d9';
      L.polyline(spec.route.map(function (s) { return [s.lat, s.lng]; }),
        { color: col, weight: 2.5, dashArray: '7,7', opacity: .85 }).addTo(map);
      spec.route.forEach(function (s, i) {
        var ic = L.divIcon({
          className: 'routenum',
          html: '<span style="background:' + col + '">' + (i + 1) + '</span>',
          iconSize: [24, 24], iconAnchor: [12, 12]
        });
        L.marker([s.lat, s.lng], { icon: ic, zIndexOffset: 1000 })
          .bindPopup('<b>' + (i + 1) + '. ' + esc(s.name) + '</b>').addTo(map);
        bounds.push([s.lat, s.lng]);
      });
    }

    if (bounds.length) map.fitBounds(bounds, { padding: [45, 45] });
    legend(map, spec);
    node.addEventListener('click', function () { map.scrollWheelZoom.enable(); });
  }

  function renderGallery(node) {
    var id = node.getAttribute('data-gallery');
    var spec = GALLERIES[id];
    if (!spec || !spec.images) { node.style.display = 'none'; return; }
    var h = '<div class="gallery">';
    spec.images.forEach(function (im) {
      h += '<figure><img src="' + attr(im.src) + '" alt="' + attr(im.alt || '') + '">' +
           (im.caption ? '<figcaption>' + esc(im.caption) + '</figcaption>' : '') + '</figure>';
    });
    h += '</div>';
    var creds = spec.images.map(function (i) { return i.credit; }).filter(Boolean);
    if (creds.length) h += '<p class="photocredit">Foto: ' + esc(creds[0]) + '.</p>';
    node.innerHTML = h;
  }

  function init() {
    document.querySelectorAll('.cls-map[data-map]').forEach(renderMap);
    document.querySelectorAll('.cls-gallery[data-gallery]').forEach(renderGallery);
    document.addEventListener('click', function (e) {
      var img = e.target.closest && e.target.closest('.gallery img, .prose figure img');
      if (!img) return;
      var ov = document.createElement('div'); ov.className = 'mm-lightbox';
      var im = new Image(); im.src = img.src;
      im.style.maxWidth = '92vw'; im.style.maxHeight = '92vh'; im.style.borderRadius = '10px';
      ov.appendChild(im); ov.addEventListener('click', function () { ov.remove(); });
      document.body.appendChild(ov);
    });
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
