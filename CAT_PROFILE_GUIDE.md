# Katzenprofil-Leitfaden

Wie ein neues Katzenprofil entsteht — von den Angaben bis zur Veröffentlichung auf GitHub Pages.
Kein Build, kein Framework: Dateien kopieren, Texte ersetzen, hochladen.

---

## 1. Benötigte Angaben pro Katze

Sammle diese Angaben, **bevor** du die Vorlage kopierst.

| Feld | Beispiel |
|---|---|
| interne ID | `2026-002` |
| Name | Ali |
| Slug (Dateiname) | `ali` |
| Status | sucht Zuhause |
| Geschlecht | männlich |
| Geburtsjahr / Schätzung | ca. 2020/2021 |
| Rasse | Mischling |
| Größe | mittel |
| Aufenthaltsregion | Region Artemida, Griechenland |
| kastriert | ja / nein / unbekannt |
| geimpft | ja / nein / unbekannt |
| FIV-/FeLV-Status | vor der Ausreise vorgesehen |
| weitere medizinische Angaben | Augen-OP, laut aktuellem Stand verheilt |
| Charaktermerkmale | sanft, menschenbezogen, friedlich |
| Verhalten mit Menschen | sucht Nähe, lässt sich hochnehmen |
| Verhalten mit Katzen | nach Beobachtung friedlich |
| Verhalten mit Hunden | *unbekannt → weglassen* |
| Erfahrung mit Kindern | *unbekannt → weglassen* |
| gewünschte Haltungsform | ruhig, nach Prüfung des Vereins |
| Balkon / Terrasse / Freigang | gesicherter Balkon willkommen |
| besondere Bedürfnisse | Rückzugsorte |
| Vorgeschichte | Fundkätzchen mit Geschwistern |
| ideales Zuhause | ruhig, mit Zeit und Nähe |
| Vermittlungsorganisation | Murka-Katzenhilfe e. V. |
| Bewerbungslink | https://murka-katzenhilfe-russland.de/Bewerbung |
| Kontakt | info@murka-katzenhilfe-russland.de |
| Hauptfoto | `<slug>-hero-960.webp` |
| Galeriefotos | `<slug>-02..`, `<slug>-03..` |
| Datum letzte Aktualisierung | 17. Juli 2026 |
| offene Punkte | FIV/FeLV-Ergebnis |
| Freigabestatus | freigegeben / in Prüfung |

### Pflichtfelder
Name · Slug · Status · Geschlecht · Geburtsjahr · Aufenthaltsregion · kastriert · geimpft ·
FIV-/FeLV-Status · Vermittlungsorganisation · Bewerbungslink · Hauptfoto · Datum

### Optionale Felder
Rasse · Größe · Verhalten mit Hunden/Kindern · besondere Bedürfnisse · Galeriefotos

---

## 2. Umgang mit unbekannten Angaben

**Grundregel: Lücken werden benannt oder weggelassen — nie ausgeschmückt.**

- Angabe unbekannt und unwichtig → **Zeile löschen**
- Angabe unbekannt und relevant → offen benennen:
  „Zum Verhalten gegenüber Hunden liegen uns keine Beobachtungen vor."
- Angabe vorläufig → kennzeichnen: „nach den bisherigen Beobachtungen …"

Nie raten, nie aus einem ähnlichen Profil übernehmen.

---

## 3. Medizinische Formulierungsregeln

**Diese Formulierungen sind nicht erlaubt:**

| Verboten | Warum |
|---|---|
| FIV/FeLV negativ | Test steht aus — das wäre eine Falschaussage |
| vollständig gesund | können wir nicht garantieren |
| garantiert verträglich | Verhalten ist keine Zusage |
| für jede Familie geeignet | Vermittlung ist eine Einzelfallprüfung |
| sofort ausreisebereit | nur mit bestätigtem Ausreisestatus |
| perfekter Familienkater | Werbesprache statt Beobachtung |
| problemlos mit allen Katzen | Verallgemeinerung |
| schmerzfrei garantiert | medizinisch nicht haltbar |

**Stattdessen:**

- „Ein FIV- und FeLV-Test wird vor der Ausreise durchgeführt."
- „Die frühere Augenproblematik wurde operativ behandelt. Laut aktuellem Informationsstand sind seine Augen gut verheilt."
- „… zeigt sich nach den bisherigen Beobachtungen friedlich gegenüber anderen Katzen."
- „Die endgültige Einschätzung erfolgt individuell im Vermittlungsprozess."

**Alter:** immer als Geburtsjahr (`ca. 2020/2021`), nie „5–6 Jahre alt" — das veraltet.

**Kitten-Regel:** Der Satz „Kitten werden nur zu zweit oder zu einem gleichaltrigen Spielpartner
vermittelt" gehört **nur** in Kitten-Profile.

**Sprache:** keine Formulierungen wie „Engel auf vier Pfoten", „tapferer Kämpfer",
„trauriges Schicksal", „bitte rette ihn", kein Mitleidsmarketing, keine Emoji-Ketten.
Die Wirkung entsteht aus der konkreten Geschichte.

---

## 4. Bildanforderungen

- **Nur echte Fotos dieser Katze.** Keine Stockfotos, keine KI-Bilder, keine fremden Katzen.
- Die Katze **nicht optisch verändern**; medizinisch relevante Merkmale **nicht retuschieren**.
- Erlaubt: Zuschnitt, Belichtung, Kompression, Schärfe — behutsam.
- Format: **WebP** (+ JPEG-Fallback), Hochformat 4:5 wirkt in den Karten am besten.
- Breiten: `480` (Karten/Galerie) und `960` (Hero/Lightbox). Nicht hochskalieren.
- `width` und `height` immer im HTML setzen → keine Layoutsprünge.
- Hero: `fetchpriority="high"`, **kein** `loading="lazy"`. Alle anderen: `loading="lazy"`.
- Alt-Texte beschreiben, was zu sehen ist. Nicht „Bild von Katze". Nicht denselben Text wiederholen.

### Bilder aufbereiten (Beispiel, Python + Pillow)

```python
from PIL import Image
im = Image.open("original.jpg").convert("RGB")   # convert() verwirft EXIF/GPS
for w in (480, 960):
    r = im.copy(); r.thumbnail((w, 10000), Image.LANCZOS)
    r.save(f"ali-02-{w}.webp", "WEBP", quality=82, method=6)
```

---

## 5. Dateibenennung

- Kleinbuchstaben, keine Leerzeichen, keine Umlaute, keine Kameradateinamen
- Profil: `katzen/<slug>.html` → z. B. `katzen/ali.html`
- Bildordner: `assets/cats/<slug>/`
- Bilder: `<slug>-hero-960.webp`, `<slug>-hero-480.webp`, `<slug>-02-960.webp`, …
- GitHub Pages ist **case-sensitive**: `Ali.html` ≠ `ali.html`

---

## 6. Datenschutzprüfung (vor jeder Veröffentlichung)

- [ ] keine genaue Adresse, keine Koordinaten, keine Route
- [ ] keine Pflegestelle erkennbar
- [ ] Ort nur als „Region Artemida, Griechenland"
- [ ] keine Chipnummer, keine Tierarztakten, keine nicht freigegebenen Befunde
- [ ] keine privaten Telefonnummern, keine Namen ohne Freigabe
- [ ] keine Koloniestandorte
- [ ] **Foto-Hintergründe geprüft**: keine Hausnummern, Klingelschilder, Kennzeichen, Straßenschilder
- [ ] **EXIF/GPS entfernt** (`.convert("RGB")` beim Speichern erledigt das)
- [ ] Fotos ausdrücklich freigegeben

---

## 7. Freigabeprozess

1. Angaben sammeln, Quelle notieren (wer hat was bestätigt?)
2. Texte nach den Regeln in Abschnitt 3 formulieren
3. Fotos aufbereiten + Datenschutzprüfung (Abschnitt 6)
4. **Margo bestätigt** Fakten und Fotofreigabe
5. Status und Bewerbungslink mit dem Verein abgleichen
6. Veröffentlichen
7. Datum der letzten Aktualisierung setzen

---

## 8. Neues Profil anlegen

1. `cat-profile-template.html` kopieren → `katzen/<slug>.html`
2. Kommentarblock ganz oben **löschen** (er ist nur Anleitung)
3. Alle `{{PLATZHALTER}}` ersetzen — danach prüfen:
   ```
   grep -n "{{" katzen/<slug>.html      # muss leer sein
   ```
4. Bilder nach `assets/cats/<slug>/` legen
5. Status setzen (Klasse **und** Text, siehe unten)
6. Canonical, Open-Graph-URL und OG-Bild auf den neuen Slug anpassen
7. JSON-LD: Name und URLs anpassen

---

## 9. Neue Karte zu `katzen.html` hinzufügen

In `katzen.html` den Block zwischen `<!-- KATZENKARTE: Ali -->` und `<!-- /KATZENKARTE -->`
kopieren und anpassen:

```html
<article class="cat-card reveal">
 <div class="cat-card__media">
  <img src="assets/cats/<slug>/<slug>-hero-960.webp" width="960" height="1200"
       loading="lazy" decoding="async" alt="<beschreibender Alt-Text>">
  <p class="cat-card__status"><span class="status status-sucht">sucht Zuhause</span></p>
 </div>
 <div class="cat-card__body">
  <h3 class="cat-card__name"><Name></h3>
  <p class="cat-card__facts"><Geschlecht> · geboren ca. <Jahr> · Region Artemida, Griechenland</p>
  <ul class="traits"><li>Merkmal 1</li><li>Merkmal 2</li><li>Merkmal 3</li></ul>
  <p class="muted" style="font-size:.92rem">Maximal zwei Sätze Vorschautext.</p>
  <a class="btn btn-primary" href="katzen/<slug>.html">&lt;Name&gt; kennenlernen
   <svg class="arrow" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
 </div>
</article>
```

Genau **drei** Merkmale, **maximal zwei Sätze** Vorschautext — sonst kippt das Kartenraster.

---

## 10. Status ändern (reserviert / vermittelt)

Immer **zwei Stellen** anpassen: `katzen.html` (Karte) und `katzen/<slug>.html` (Hero + Faktenblock).

| Status | HTML |
|---|---|
| sucht Zuhause | `<span class="status status-sucht">sucht Zuhause</span>` |
| in Klärung | `<span class="status status-klaerung">in Klärung</span>` |
| reserviert | `<span class="status status-reserviert">reserviert</span>` |
| vermittelt | `<span class="status status-vermittelt">vermittelt</span>` |
| derzeit nicht vermittelbar | `<span class="status status-nicht">derzeit nicht vermittelbar</span>` |

Klasse **und** Text müssen zusammenpassen — die Farbe allein trägt die Information nicht (Barrierefreiheit).

Bei **vermittelt**: Profil online lassen (die Geschichte zeigt, dass Vermittlung gelingt), aber
den Bewerbungs-Button entfernen oder deutlich als beendet kennzeichnen. Datum aktualisieren.

---

## 11. Veröffentlichen (GitHub)

Hochladen ins Repository-Root:

```
katzen.html                      (aktualisiert: neue Karte)
katzen/<slug>.html               (neu)
assets/cats/<slug>/…             (neu, alle Bilder)
```

Danach live prüfen:
- `https://www.margoanimalcare.org/katzen.html` → Karte sichtbar, Bild lädt
- `https://www.margoanimalcare.org/katzen/<slug>.html` → Bilder, Links, Lightbox
- Browser-Konsole: keine Fehler
- Handy: Darstellung ab 360 px Breite

---

## 12. Wiederkehrende Prüfliste vor jedem Upload

- [ ] keine `{{Platzhalter}}` mehr in der Datei
- [ ] keine erfundenen Fakten, keine medizinischen Garantien
- [ ] Alter als Geburtsjahr
- [ ] Kitten-Regel nur bei Kitten
- [ ] „Margo" durchgängig (nicht mit „Margarita" mischen)
- [ ] Murka-Angaben korrekt geschrieben
- [ ] kein exakter Standort
- [ ] alle Bilder vorhanden, Alt-Texte gesetzt, `width`/`height` gesetzt
- [ ] alle Links funktionieren, externe mit `target="_blank" rel="noopener noreferrer"`
- [ ] Datum der letzten Aktualisierung gesetzt
