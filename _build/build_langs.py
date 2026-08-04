#!/usr/bin/env python3
"""
Erzeugt die englische und griechische Fassung aus den deutschen Seiten.

Prinzip: Layout, Struktur und alle Bausteine bleiben unverändert.
Ersetzt werden ausschliesslich Texte, Pfade und Sprachmetadaten.
Dadurch sind alle Sprachfassungen gleichwertig.

Aufruf:  python3 _build/build_langs.py
"""
import os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://www.margoanimalcare.org/"

# Seiten, die in alle Sprachen übernommen werden
PAGES = [
    "index.html", "unsere-arbeit.html", "katzen.html", "mitmachen.html",
    "foerdern.html", "wirkung-transparenz.html", "partner.html", "route.html",
    "unterstuetzen.html", "kontakt.html", "impressum.html", "datenschutz.html",
    "404.html",
]
SUBDIR_PAGES = [
    "rollen/field-care.html", "rollen/vet-transport.html", "rollen/farm-care.html",
    "rollen/farm-support.html", "rollen/funding-scout.html",
    "rollen/transparency.html", "rollen/communication.html",
]
CAT_PAGES = [
    "katzen/ali.html", "katzen/benno.html", "katzen/findus.html",
    "katzen/albalouise.html", "katzen/felia.html", "katzen/indigo.html",
    "katzen/mahalo.html", "katzen/mara.html", "katzen/metaxi.html",
    "katzen/susi.html", "katzen/willow.html",
]

LANGS = {
    "en": {"locale": "en_GB", "label": "English"},
    "el": {"locale": "el_GR", "label": "Ελληνικά"},
}


def fix_asset_paths(html, depth_extra=1):
    """Assets liegen weiterhin im Wurzelverzeichnis -> eine Ebene höher verweisen."""
    prefix = "../" * depth_extra
    # href und src
    html = re.sub(r'(href|src)="(?!https?:|mailto:|#|\.\./)(assets/)', rf'\1="{prefix}\2', html)
    # srcset enthält mehrere kommagetrennte Pfade mit Breitenangabe
    def _srcset(m):
        parts = []
        for item in m.group(2).split(','):
            item = item.strip()
            if item.startswith('assets/'):
                item = prefix + item
            parts.append(item)
        return f'{m.group(1)}="' + ', '.join(parts) + '"'
    html = re.sub(r'(srcset)="([^"]+)"', _srcset, html)
    return html


def set_lang_meta(html, lang, page_path, locale):
    """Sprachattribut, Canonical, hreflang und og:locale setzen."""
    html = re.sub(r'<html[^>]*lang="[a-zA-Z-]*"', f'<html lang="{lang}"', html, count=1)

    canonical = f"{BASE_URL}{lang}/{page_path}"
    html = re.sub(r'<link rel="canonical"[^>]*>',
                  f'<link rel="canonical" href="{canonical}">', html, count=1)
    html = re.sub(r'<meta property="og:url"[^>]*>',
                  f'<meta property="og:url" content="{canonical}">', html, count=1)
    html = re.sub(r'<meta property="og:locale"[^>]*>',
                  f'<meta property="og:locale" content="{locale}">', html, count=1)

    # hreflang-Verweise auf alle Sprachfassungen
    alts = (f'<link rel="alternate" hreflang="de" href="{BASE_URL}{page_path}">\n'
            f'<link rel="alternate" hreflang="en" href="{BASE_URL}en/{page_path}">\n'
            f'<link rel="alternate" hreflang="el" href="{BASE_URL}el/{page_path}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{page_path}">')
    html = re.sub(r'<link rel="canonical"[^>]*>',
                  lambda m: m.group(0) + "\n" + alts, html, count=1)
    return html


def add_hreflang_to_german(html, page_path):
    """Auch die deutschen Seiten erhalten hreflang-Verweise."""
    if 'hreflang="de"' in html:
        return html
    alts = (f'<link rel="alternate" hreflang="de" href="{BASE_URL}{page_path}">\n'
            f'<link rel="alternate" hreflang="en" href="{BASE_URL}en/{page_path}">\n'
            f'<link rel="alternate" hreflang="el" href="{BASE_URL}el/{page_path}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{page_path}">')
    return re.sub(r'<link rel="canonical"[^>]*>',
                  lambda m: m.group(0) + "\n" + alts, html, count=1)


LANG_SWITCH_CSS = """
  /* Sprachumschalter */
  .site-lang-switch{display:flex;align-items:center;gap:2px;font-size:.76rem;
    border:1px solid var(--hair);border-radius:6px;overflow:hidden}
  .site-lang-switch a{padding:4px 8px;color:var(--ink-soft);text-decoration:none;
    line-height:1;transition:background .2s var(--ease),color .2s var(--ease)}
  .site-lang-switch a:hover{background:var(--petrol-tint);color:var(--petrol)}
  .site-lang-switch a[aria-current="true"]{background:var(--petrol);color:#fff;font-weight:600}
  @media(max-width:899px){.site-lang-switch{display:none}}
  .site-drawer__langs{display:flex;gap:8px;margin-top:20px;padding-top:18px;
    border-top:1px solid var(--hair-warm)}
  .site-drawer__langs a{flex:1;text-align:center;padding:10px;border:1px solid var(--hair);
    border-radius:7px;color:var(--ink-soft);text-decoration:none;font-size:.9rem}
  .site-drawer__langs a[aria-current="true"]{background:var(--petrol);color:#fff;
    border-color:var(--petrol);font-weight:600}
"""


def build_lang_switch(current_lang, page_path, depth):
    """Baut den Sprachumschalter für Kopfzeile und Mobilmenü."""
    up = "../" * depth
    targets = {
        "de": f"{up}{'../' if current_lang != 'de' else ''}{page_path}",
        "en": f"{up}{'' if current_lang != 'de' else ''}{'../' if current_lang != 'de' else ''}en/{page_path}",
        "el": f"{up}{'../' if current_lang != 'de' else ''}el/{page_path}",
    }
    if current_lang == "de":
        targets = {"de": f"{up}{page_path}", "en": f"{up}en/{page_path}", "el": f"{up}el/{page_path}"}
    else:
        base = up + "../"
        targets = {"de": f"{base}{page_path}", "en": f"{base}en/{page_path}", "el": f"{base}el/{page_path}"}

    labels = {"de": "DE", "en": "EN", "el": "ΕΛ"}
    full = {"de": "Deutsch", "en": "English", "el": "Ελληνικά"}

    desktop = '<div class="site-lang-switch" role="group" aria-label="Sprache / Language">'
    drawer = '<div class="site-drawer__langs" role="group" aria-label="Sprache / Language">'
    for code in ("de", "en", "el"):
        cur = ' aria-current="true"' if code == current_lang else ''
        desktop += f'<a href="{targets[code]}" hreflang="{code}" lang="{code}"{cur}>{labels[code]}</a>'
        drawer += f'<a href="{targets[code]}" hreflang="{code}" lang="{code}"{cur}>{full[code]}</a>'
    desktop += '</div>'
    drawer += '</div>'
    return desktop, drawer


def inject_lang_switch(html, current_lang, page_path, depth):
    """Setzt den Sprachumschalter in Kopfzeile und Mobilmenü ein."""
    if 'site-lang-switch' in html:
        return html
    desktop, drawer = build_lang_switch(current_lang, page_path, depth)

    # CSS ergänzen
    if '.site-lang-switch' not in html:
        html = re.sub(r'</style>', LANG_SWITCH_CSS + '  </style>', html, count=1)

    # Desktop: vor dem CTA-Button in den Aktionen
    html = re.sub(r'(<div class="site-header__actions">)',
                  r'\1\n      ' + desktop, html, count=1)
    # Mobil: im Menü-Fuss
    html = re.sub(r'(<div class="site-drawer__foot">)',
                  drawer + r'\n    \1', html, count=1)
    return html
