#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut eine einzelne Seite in allen Zielsprachen."""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_langs import fix_asset_paths, set_lang_meta, inject_lang_switch, LANGS, add_hreflang_to_german
from apply import apply_translations, find_untranslated

def build(page, dicts, depth=0):
    """page: relativer Pfad wie 'mitmachen.html'; dicts: {'en': (common, page), ...}"""
    src = open(page, encoding='utf-8').read()
    results = {}
    for lang, (common, pagedict) in dicts.items():
        html = fix_asset_paths(src, 1)
        html = set_lang_meta(html, lang, page, LANGS[lang]['locale'])
        html = re.sub(r'<div class="site-lang-switch".*?</div>', '', html, flags=re.S, count=1)
        html = re.sub(r'<div class="site-drawer__langs".*?</div>', '', html, flags=re.S, count=1)
        html = inject_lang_switch(html, lang, page, depth)
        # Titel und Beschreibung stehen in Attributen -> separat ersetzen
        for de_txt, tgt in pagedict.items():
            for attr in ('content="', 'alt="', 'aria-label="', 'title="'):
                html = html.replace(attr + de_txt + '"', attr + tgt + '"')
        html, h1, m1 = apply_translations(html, pagedict, report=True)
        html, h2, m2 = apply_translations(html, common, report=True)
        # Rückfall: Links auf noch nicht übersetzte Seiten zeigen auf die deutsche Fassung.
        # Sobald die Übersetzung existiert, greift beim nächsten Bauen automatisch der lokale Pfad.
        def _fallback(m):
            target = m.group(1)
            if target.startswith(('http', 'mailto:', '#', '../')):
                return m.group(0)
            if os.path.exists(os.path.join(lang, target)):
                return m.group(0)
            return 'href="../' + target + '"'
        html = re.sub(r'href="([^"#?:]+\.html)"', _fallback, html)

        out = os.path.join(lang, page)
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        open(out, 'w', encoding='utf-8').write(html)
        rest = find_untranslated(html)
        results[lang] = dict(hits=h1+h2, missing=m1, rest=rest)
    # Deutsche Seite: hreflang + Umschalter sicherstellen
    de = add_hreflang_to_german(src, page)
    de = inject_lang_switch(de, 'de', page, depth)
    open(page, 'w', encoding='utf-8').write(de)
    return results
