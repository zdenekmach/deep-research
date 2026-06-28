#!/usr/bin/env python3
"""Concept Learning Site generator — topic-agnostic.

Vezme content.md a web_template.html → vygeneruje standalone offline index.html
a zkopiruje assets/ (marked.min.js, mermaid.min.js) vedle nej.

Titul:
  1. --title "Muj titul"  (explicitni argument)
  2. frontmatter title: ... v content.md
  3. prvni H1 radek (# ...) v content.md
  4. fallback "Studijni pruvodce"

Usage:
  python3 gen.py                          # content.md + web_template.html v cwd
  python3 gen.py --content path/content.md --out path/out/
  python3 gen.py --title "Moje tema" --subtitle "studijni pruvodce"
  python3 gen.py --content c.md --template tmpl.html --out ./site/
"""
import argparse
import json
import re
import shutil
from pathlib import Path

SKILL_ASSETS = Path(__file__).parent  # directory containing gen.py and the .min.js files


def extract_title_from_content(text: str) -> str | None:
    """Try frontmatter title: or first # heading."""
    # frontmatter title: "..."  or  title: ...
    fm = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if fm:
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm.group(1), re.MULTILINE)
        if m:
            return m.group(1).strip()
    # first H1
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    if m:
        # strip version/date annotations like "— Studijni material" or " | v1.0"
        title = m.group(1).strip()
        title = re.split(r'\s*[—–|]\s*', title)[0].strip()
        return title
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate offline concept learning site")
    parser.add_argument("--content", default="content.md",
                        help="Path to content markdown (default: content.md in cwd)")
    parser.add_argument("--template", default=None,
                        help="Path to web_template.html (default: same dir as gen.py)")
    parser.add_argument("--out", default=None,
                        help="Output directory (default: same dir as content.md)")
    parser.add_argument("--title", default=None,
                        help="Site title (overrides auto-detection)")
    parser.add_argument("--subtitle", default="studijni pruvodce",
                        help="Site subtitle shown after dash (default: 'studijni pruvodce')")
    parser.add_argument("--version", default="v1.0.0",
                        help="Version string shown in header (default: v1.0.0)")
    parser.add_argument("--data", default=None,
                        help="Path to site.json (maps/galleries data). Enables the data-driven "
                             "site_engine. If omitted, falls back to plain markdown rendering.")
    args = parser.parse_args()

    content_path = Path(args.content).resolve()
    if not content_path.exists():
        raise FileNotFoundError(f"content.md not found: {content_path}")

    # Template selection: explicit --template wins; else site_template (when --data) or web_template.
    if args.template:
        template_path = Path(args.template).resolve()
    elif args.data:
        template_path = SKILL_ASSETS / "site_template.html"
    else:
        template_path = SKILL_ASSETS / "web_template.html"
    if not template_path.exists():
        raise FileNotFoundError(f"template not found: {template_path}")

    out_dir = Path(args.out).resolve() if args.out else content_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    content_text = content_path.read_text(encoding="utf-8")
    template_text = template_path.read_text(encoding="utf-8")

    # Determine title
    title = args.title or extract_title_from_content(content_text) or "Studijni pruvodce"

    # Safe embed: break any </script> in content
    safe_content = content_text.replace("</script>", "<\\/script>")

    # Load + sanitize site data (maps/galleries). Re-dump to validate JSON; break </script.
    site_data = "{}"
    if args.data:
        data_path = Path(args.data).resolve()
        if not data_path.exists():
            raise FileNotFoundError(f"site.json not found: {data_path}")
        parsed = json.loads(data_path.read_text(encoding="utf-8"))  # validates
        site_data = json.dumps(parsed, ensure_ascii=False).replace("</", "<\\/")

    # Substitute placeholders
    html = template_text
    html = html.replace("__TITLE__", title)
    html = html.replace("__SUBTITLE__", args.subtitle)
    html = html.replace("__VERSION__", args.version)
    html = html.replace("__CONTENT__", safe_content)
    html = html.replace("__SITEDATA__", site_data)

    out_html = out_dir / "index.html"
    out_html.write_text(html, encoding="utf-8")

    # Copy assets/ (marked.min.js, mermaid.min.js) next to index.html
    src_assets = SKILL_ASSETS  # gen.py lives alongside the .min.js files
    out_assets = out_dir / "assets"
    out_assets.mkdir(exist_ok=True)
    assets_to_copy = ["marked.min.js", "mermaid.min.js"]
    if "site_engine.js" in template_text:
        assets_to_copy.append("site_engine.js")
    for js in assets_to_copy:
        src = src_assets / js
        dst = out_assets / js
        if src.exists():
            shutil.copy2(src, dst)
        else:
            print(f"WARNING: {src} not found — HTML will reference a missing file")

    kb = out_html.stat().st_size / 1024
    print(f"OK -> {out_html}  ({kb:.1f} KB)")
    print(f"     assets/ -> {out_assets}/  ({', '.join(assets_to_copy)})")
    print(f"     title: {title!r}" + (f"  | data: {args.data}" if args.data else ""))


if __name__ == "__main__":
    main()
