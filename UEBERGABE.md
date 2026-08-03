# Übergabe und Pflegeanleitung

**Margo Animal Care Initiative · Website 3.0**
Stand: 2. August 2026

Dieses Dokument beschreibt, wie die Website aufgebaut ist, wie Inhalte gepflegt werden, wie veröffentlicht wird und wie sich Änderungen rückgängig machen lassen. Es richtet sich an alle, die künftig an der Seite arbeiten — auch ohne Vorkenntnisse.

---

## 1. Aufbau in Kürze

Die Website besteht aus einzelnen HTML-Dateien ohne Datenbank und ohne Redaktionssystem. Das ist bewusst so: Es gibt nichts, was ausfallen, gehackt oder teuer werden kann. Wer eine Textstelle ändern will, öffnet die Datei und ändert den Text.

```
index.html                  Startseite
unsere-arbeit.html          Geschichte, Arbeitsweise, Roadmap
katzen.html                 Übersicht der Katzen
mitmachen.html              Einsatzarten, Rollen, Einstieg
foerdern.html               Governance, Mittelverwendung, Kastration
wirkung-transparenz.html    Kosten, Zuständigkeiten
unterstuetzen.html          Kurzer Entscheidungs-Hub
partner.html                Partner mit Kontaktangaben
route.html                  Bildreise durch die Versorgungsorte
kontakt.html                Zuständigkeiten
impressum.html              noch zu vervollständigen
datenschutz.html            noch rechtlich zu prüfen
404.html                    Fehlerseite

katzen/                     14 Katzenprofile + Vorlage
rollen/                     7 Rollenbeschreibungen
assets/css/                 site.css · tw.css · fonts.css · cats.css
assets/js/                  site.js · lucide.min.js
assets/fonts/               16 Schriftdateien
assets/hero/                Bilder der Startseite
assets/cats/                Katzenfotos
assets/journey/             Bilder der Versorgungsroute
sitemap.xml · robots.txt
```

Dazu kommen **Weiterleitungsseiten** für alte Adressen (`ansatz.html`, `volunteer.html`, `veterinaerkosten.html`, `immersive-reise.html`, `margo-oeffentlich.html`, `volunteer-*.html`). Sie leiten automatisch auf die neuen Adressen weiter. **Bitte nicht löschen** — sonst laufen bestehende Links und Suchtreffer ins Leere.

---

## 2. Die vier wichtigsten Regeln

**1 · Nichts veröffentlichen, was nicht belegt ist.**
Jede Zahl braucht Definition, Zeitraum und Quelle. Ist eine Angabe unsicher, wird sie als Schätzung gekennzeichnet. Ist sie unbekannt, wird der ganze Block ausgeblendet — **niemals ein sichtbarer Platzhalter wie `[X]`**.

**2 · Keine genauen Standorte.**
Weder Plus Codes noch Adressen von Farm, privaten Versorgungsstellen oder Kolonien. Immer nur „Region Artemida/Athen". Das schützt die Tiere und die Menschen dort.

**3 · Keine erfundenen Zitate, Zahlen oder Versprechen.**
Auch keine Antwortzeiten oder Zusagen, die nicht sicher eingehalten werden können.

**4 · Schreibweise: `ss` statt `ß`.**
Durchgehend im gesamten Text. Ausnahme: Eigennamen wie „Karl-Friedrich-Straße".

---

## 3. Inhalte pflegen

### Eine Zahl aktualisieren
Kennzahlen stehen in Karten mit einem Statusabzeichen:

```html
<span class="status status--verified">Verifiziert</span>   <!-- belegt -->
<span class="status status--estimated">Schätzung</span>    <!-- Näherung -->
```

Ändert sich eine Zahl, immer auch den Zeitraum darunter anpassen. Ist eine Zahl noch nicht belegt, den ganzen Block in einen Kommentar setzen statt ihn leer zu lassen:

```html
<!-- AUSGEBLENDET bis verifiziert (F1)
     ... Block hier ...
-->
```

### Eine neue Katze anlegen
1. `katzen/cat-profile-template.html` kopieren und nach `katzen/name.html` umbenennen.
2. Fotos nach `assets/cats/name/` legen, als WebP in zwei Breiten (480 und 960 px).
3. Texte, Bildbeschreibungen und Gesundheitsangaben eintragen — offene Punkte ausdrücklich benennen, nicht weglassen.
4. Auf `katzen.html` eine Karte im Abschnitt „Diese Katzen stellen wir vor" ergänzen (bestehende Karte kopieren).
5. In `sitemap.xml` eine Zeile ergänzen.

Ausführlich beschrieben in `katzen/CAT_PROFILE_GUIDE.md`.

### Eine Rolle ändern oder schliessen
Die Rollenseiten liegen in `rollen/`. Das Statusabzeichen oben ändern:

```html
<span class="status status--verified" data-role-status>Offen</span>
```
Bei Besetzung auf „Besetzt" ändern, bei Pause auf „Pausiert". Die Rolle bleibt sichtbar, damit klar ist, dass sie existiert — aber niemand bewirbt sich vergeblich.

### Bilder hinzufügen
Immer als WebP, nie als PNG oder JPG in Originalgrösse. Umrechnung:

```bash
python3 -c "
from PIL import Image
im = Image.open('bild.png').convert('RGB')
for w in (720, 1200):
    h = int(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(f'bild-{w}.webp', 'WEBP', quality=82, method=6)
"
```

Jedes Bild braucht ein `alt`-Attribut, das beschreibt, was zu sehen ist — nicht „Foto" oder „Bild".

---

## 4. Nach Änderungen: Tailwind neu bauen

**Wichtig:** Die Gestaltung nutzt Tailwind-Klassen (z. B. `grid`, `md:grid-cols-2`, `max-w-[1160px]`). Diese sind in `assets/css/tw.css` vorkompiliert — es sind nur die Klassen enthalten, die tatsächlich verwendet werden.

**Wird eine neue Tailwind-Klasse in einer HTML-Datei verwendet, wirkt sie erst nach einem Neubau.**

```bash
npm install tailwindcss@3.4.17
npx tailwindcss -c tailwind.config.js -i input.css -o assets/css/tw.css --minify
```

Mit dieser `tailwind.config.js`:
```js
module.exports = {
  content: ['./**/*.html'],
  theme: { extend: {} },
}
```
Und dieser `input.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Wer keine neuen Tailwind-Klassen verwendet, sondern nur Texte ändert, muss nichts neu bauen.

---

## 5. Veröffentlichen

Die Seite läuft auf GitHub Pages, Repository `Artemsenik/Margo-org`, Domain über die Datei `CNAME`.

```bash
git add -A
git commit -m "Beschreibung der Änderung"
git push
```
Nach etwa ein bis zwei Minuten ist die Änderung live.

### Vor jeder Veröffentlichung prüfen
- [ ] Keine sichtbaren `[X]`-Platzhalter
- [ ] Keine genauen Standortangaben
- [ ] Alle neuen Bilder haben eine Bildbeschreibung
- [ ] Alle neuen Links funktionieren
- [ ] Auf dem Handy angesehen (kein Querscrollen)
- [ ] Bei neuen Tailwind-Klassen: `tw.css` neu gebaut

### Rückgängig machen
```bash
git log --oneline          # Änderungen ansehen
git revert <commit-id>     # eine bestimmte Änderung zurücknehmen
git push
```
`git revert` ist sicherer als `git reset`, weil die Historie erhalten bleibt.

---

## 6. Was vor dem Start noch fehlt

| # | Was | Wer liefert | Blockiert |
|---|---|---|---|
| **B2** | Betreiberangaben fürs Impressum, rechtliche Prüfung der Datenschutzerklärung | Verantwortliche Person | **Ja — Start** |
| F1 | Kastrationen bisher/ausstehend, Kosten je Eingriff | Margo + Praxen | Kastrationsmodule |
| F2 | Höhe der Schutzgebühr, übliche Dauer | Murka e. V. | Vermittlungsabschnitt |
| F3 | Geplante Kastrationsaktion: Zeitraum, Anzahl, Budget | Margo | Förderseite |
| F6 | Bestätigung der Veterinärzahlen | Margo + Praxen | — (bereits als verifiziert ausgewiesen) |
| F7 | Aktueller Freistellungsbescheid, vertragliche Rolle des Vereins | Murka e. V. | Governance-Abschnitt |
| F9 | Margos eigenes Statement | Margo | Startseite und „Unsere Arbeit" |
| F10 | Farm-Fotos für die reservierten Bildbereiche | Margo | Rollenseiten |
| F12 | Realistische Antwortzeit auf Anfragen | Team | Footer und Kontaktseite |
| F13 | Ansprechpartner je Rolle | Team | Rollenkarten |

Die beiden Rechtsseiten stehen derzeit auf `noindex` und erscheinen nicht in Suchmaschinen. Das ist bewusst so, bis die Angaben vollständig sind.

---

## 7. Was bewusst nicht gebaut wurde

**Kein Bewerbungsformular.** Statisches Hosting kann Formulare nur über einen externen Dienst verarbeiten — der würde wieder Besucherdaten an Dritte übertragen. Der Einstieg läuft deshalb über vorbefüllte E-Mails. Ein Formular lohnt sich erst, wenn das Anfragevolumen unübersichtlich wird; dann sollte ein in der EU gehosteter Anbieter gewählt werden.

**Kein Fortschrittsbericht und kein Archiv.** Es ist noch kein Berichtszeitraum abgeschlossen. Statt einen Bericht vorzutäuschen, benennt die Transparenzseite offen, was vorliegt und was fehlt. Sobald der erste Bericht existiert, kann er dort ergänzt werden.

**Keine Schulklassen-, Touristen- oder Firmeneinsatztage als festes Angebot.** Diese brauchen geklärte Aufsicht, Versicherung und Betreuungskapazität. Bis dahin wird nichts angekündigt, was nicht getragen werden kann.

**Kein Care Center als Bauprojekt.** Es ist als „langfristige Option in Prüfung" dargestellt, mit den offenen Voraussetzungen. Erst wenn Bedarf, Standortrecht, Genehmigungen, Budget, Personalmodell und tiermedizinische Standards geklärt sind, kann daraus ein förderbares Vorhaben werden.

---

## 8. Technische Eckdaten

- **Keine Übertragung an Dritte.** Schriften, Symbole und Gestaltung werden lokal ausgeliefert. Gemessen: 0 externe Anfragen auf allen 48 Seiten.
- **Kein Tracking, keine Cookies, keine Nutzerkonten.**
- **Zugänglichkeit:** Sprungmarke zum Inhalt, sichtbarer Fokusrahmen, vollständige Tastaturbedienung, Menü mit Fokusbindung und Escape, `aria-current` auf dem aktiven Menüpunkt, alle Kontraste über der WCAG-AA-Schwelle.
- **Bildgewicht:** Alle Startseitenbilder als WebP in zwei Auflösungen; das Hero-Bild wiegt 52 KB statt 1,85 MB.
- **Gestaltung:** 11 KB kompiliertes Tailwind statt CDN-Laufzeit.
