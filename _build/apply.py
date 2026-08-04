#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Robustes Ersetzen von Texten in HTML.

Problem: Im Quelltext sind Sätze über mehrere Zeilen umbrochen und eingerückt.
Ein einfaches str.replace() mit normalisiertem Text findet sie deshalb nicht.

Lösung: Der deutsche Suchtext wird in ein Regex übersetzt, in dem jede
Leerraumfolge auf beliebigen Leerraum passt. Die ursprüngliche Einrückung
bleibt dadurch erhalten, ohne dass die Wörterbücher Umbrüche kennen müssen.
"""
import re


def _to_pattern(text):
    """
    Deutscher Text -> Regex mit flexiblem Leerraum.
    Der Treffer muss einen VOLLSTÄNDIGEN Textknoten bilden, also zwischen
    '>' und '<' stehen. Sonst würden kurze Wörter wie 'Futter' oder 'Partner'
    auch mitten in noch unübersetzten Sätzen ersetzt.
    """
    parts = [re.escape(p) for p in text.split()]
    core = r'\s+'.join(parts)
    return re.compile(r'(?<=>)(\s*)' + core + r'(\s*)(?=<)')


def apply_translations(html, mapping, report=False):
    """
    Ersetzt alle Einträge des Wörterbuchs. Längere Texte zuerst,
    damit kurze Teilstrings nicht vorzeitig greifen.
    Umgebender Leerraum bleibt erhalten.
    """
    hits, misses = 0, []
    for de in sorted(mapping, key=len, reverse=True):
        target = mapping[de]
        pat = _to_pattern(de)
        html, n = pat.subn(lambda m: m.group(1) + target + m.group(2), html)
        if n:
            hits += n
        else:
            misses.append(de)
    if report:
        return html, hits, misses
    return html


def find_untranslated(html, lang='en'):
    """
    Sucht nach verbliebenem deutschem Text im sichtbaren Bereich.
    Grobe Heuristik über typische Funktionswörter.
    """
    import html as H
    body = html[html.find('<body'):]
    body = re.sub(r'<(script|style).*?</\1>', '', body, flags=re.S)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    marker = re.compile(
        r'\b(und|oder|der|die|das|für|mit|von|werden|wird|nicht|sind|eine|einer|'
        r'einen|auf|dem|den|des|ist|kann|können|über|durch|bei|aus|zum|zur|'
        r'wir|uns|unsere|jede|jeder|jedes|dass|damit|sowie|bereits)\b')
    out = []
    for t in re.findall(r'>([^<>]{4,})<', body):
        t2 = H.unescape(re.sub(r'\s+', ' ', t)).strip()
        if t2 and marker.search(t2):
            out.append(t2)
    return out
