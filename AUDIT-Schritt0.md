# STATUSBERICHT — Schritt 0: Repository- und Live-Audit

**Projekt:** Margo Animal Care Initiative · Website-Relaunch 3.0
**Grundlage:** Umsetzungsauftrag 3.0 (verbindlich), Strukturentwurf 2.0 (Inhaltsbasis)
**Datum:** 2. August 2026
**Arbeitsstand:** Arbeitskopie erstellt, Produktivstand unverändert

---

## 1. Erledigt

- Arbeitskopie aus dem Deploy-Export erstellt (neuer als GitHub-Stand `9b090c1`, 24.07.2026). Produktivstand bleibt reproduzierbar.
- Vollständiges Datei- und Inhaltsinventar: 18 HTML-Seiten, 14 Katzenprofile, Bild-Assets, 1 CSS-Datei.
- Sicherheitsprüfung auf Standortdaten, personenbezogene Daten, Zahlungswege.
- Faktenprüfung gegen Abschnitt 2 des Auftrags (Platzhalter, unbelegte Angaben).
- Prüfung von Navigation, Mobile-Verhalten, Metadaten, Accessibility-Grundlagen, externen Diensten, Rechtsseiten.
- Abgleich Auftrag 3.0 gegen Entwurf 2.0; Abweichungen dokumentiert (Abschnitt 5).

---

## 2. Bestandsaufnahme

### Dateien und Zuordnung

| Datei | Rolle heute | Ziel 3.0 |
|---|---|---|
| `index.html` | dünne Landing (intern wirkend) | `index.html` (verschmolzen) |
| `margo-oeffentlich.html` | faktische Startseite, 12 Abschnitte | verschmelzen + Tiefe verteilen |
| `ansatz.html` | Prinzipien, Wirkung, 5 Systeme | `unsere-arbeit.html` |
| `katzen.html` + `katzen/` (14) | Übersicht + Profile | bleibt, Reihenfolge drehen |
| `volunteer.html` + 7 Rollenseiten | Mithelfen | `mitmachen.html` + `/rollen/` |
| `foerdern.html` | Spenden | `foerdern.html` (Privat/Organisation trennen) |
| `partner.html` | Partner | bleibt als Belegseite |
| `veterinaerkosten.html` | Kostentransparenz | `wirkung-transparenz.html` |
| `immersive-reise.html` | Bildreise, 13 Stationen | `route.html` |
| `en.html` | isolierte EN-Einzelseite | `/en/` Kernseiten (Phase 3) |
| `margo-zugang.html` | interner Zugang | Audit-Entscheidung offen |

### Externe Dienste (alle Third-Party-Requests)
- `cdn.tailwindcss.com` (Tailwind Play-CDN)
- `fonts.googleapis.com` / `fonts.gstatic.com` (Google Fonts)
- `cdn.jsdelivr.net` (Lucide Icons)
- `images.unsplash.com` (Stockfotos)

### Formulare
Keine. Alle Kontaktwege laufen über `mailto:` bzw. externe Links. Für Abschnitt 10 des Auftrags (Formulare, Bestätigungen, Routing) existiert noch keine Grundlage.

---

## 3. Befunde nach Schweregrad

### BLOCKER — vor Veröffentlichung zwingend

**B1 · Exakter Standort der Farm öffentlich (MUSS-Verstoss)**
Der Plus Code `XXHH+P3C Ag. Serafim` steht sichtbar in `ansatz.html` (Bildunterschrift) und `foerdern.html` (Standortangabe). `foerdern.html` nennt zusätzlich „Elternhaus, Zweitsitz, Surfschule und vier Kolonien".
Besonders zu beachten: `immersive-reise.html` verspricht ausdrücklich, *keine* exakten Plus Codes zu zeigen. Die Seite widerspricht sich selbst.
→ *Massnahme:* Plus Code entfernen, Angabe auf „Region Artemida/Athen" reduzieren.

**B2 · Rechtsseiten fehlen vollständig**
Weder `impressum.html` noch `datenschutz.html` noch `404.html` existieren. Bei EU-Adressierung mit Spendenaufruf ist das ein rechtliches Risiko.
→ *Massnahme:* Vor Launch erstellen; Inhalte müssen vom Verantwortlichen bestätigt werden.

**B3 · Sichtbare Platzhalter im öffentlichen Build**
16 `[X]`-Platzhalter: `foerdern.html` (10 — Kastrationszahlen, Kosten, geplante Aktion), `en.html` (4), `katzen.html` (2 — Schutzgebühr).
Der Auftrag verlangt: unbestätigte Elemente **ausblenden**, nie als Platzhalter zeigen.
→ *Massnahme:* Betroffene Module bis zur Verifikation ausblenden.

### HOCH

**H1 · Datenschutz durch Third-Party-Requests**
Google Fonts, Tailwind-CDN, jsDelivr und Unsplash übertragen bei jedem Aufruf die IP-Adresse an Dritte — ohne Einwilligung und ohne Datenschutzerklärung.
→ *Massnahme:* Fonts und Icons lokal einbinden; Tailwind zur Build-Zeit kompilieren.

**H2 · Stockfotos auf den Kernseiten**
`index.html` (2) und `margo-oeffentlich.html` (4) nutzen Unsplash-Bilder. Das untergräbt die Authentizität, die den Auftritt trägt — echte Fotos existieren bereits in `assets/cats/` und `assets/journey/`.
→ *Massnahme:* Durch echte Medien ersetzen oder Bildbereich weglassen.

**H3 · Zahlungsweg ungeprüft öffentlich**
IBAN `DE43 4306 0129 0…` (Volksbank Bochum Witten) steht offen in `foerdern.html`.
→ *Massnahme:* Schriftliche Bestätigung von Murka-Katzenhilfe e. V. einholen, dass Konto, Verwendungszweck und Spendenquittungsweg korrekt sind.

**H4 · Keine mobile Navigation**
Die Leiste ist `hidden md:flex`. Auf dem Handy sind ausser Logo und Button **keine** Navigationspunkte erreichbar. Bei mobiler Mehrheitsnutzung ist das der grösste Usability-Defekt.

**H5 · Navigation uneinheitlich**
`katzen.html` ohne EN-Button · `volunteer.html` mit abweichender Kurzleiste und Logo-Link auf `index.html` · `immersive-reise.html` ohne Leiste. Zwei redundante Anker („So arbeiten wir", „Mitwirken").

**H6 · Sprachschalter ohne Äquivalent**
Der EN-Button auf fünf Seiten führt immer auf dieselbe Einzelseite `en.html`, nicht auf die entsprechende Übersetzung. Verstösst gegen „Keine leeren Sprachschalter".

### MITTEL

**M1 · Metadaten unvollständig** — Nur `katzen.html` hat Canonical, OG-Tags, Skip-Link und `aria-current`. Alle anderen acht Seiten: keine. Keine `sitemap.xml`, keine `robots.txt`.

**M2 · Rechtschreibung gemischt** — 14 Dateien enthalten `ß`, während `veterinaerkosten.html` bereits durchgängig `ss` verwendet („regelmässig", „Massnahmen"). Der Auftrag verlangt einheitlich `ss`.

**M3 · Startseite überladen** — 12 Abschnitte, ~15 KB Text. Der 30-Sekunden-Erfolgstest ist so nicht erfüllbar.

**M4 · Bildbestand ungleich** — `findus` hat 3 Bilder, andere Katzen deutlich mehr. Mehrere „Bereich reserviert"-Blöcke warten auf Farm-Fotos.

---

## 4. Offene Fakten und Freigaben

| # | Angabe | Status | Wer bestätigt |
|---|---|---|---|
| F1 | Kastrationen bisher / ausstehend / Kosten je Eingriff | OFFEN | Margo + Partnerpraxen |
| F2 | Schutzgebühr Vermittlung | OFFEN | Murka-Katzenhilfe e. V. |
| F3 | Geplante Kastrationsaktion (Zeitraum, Anzahl, Budget) | OFFEN | Margo |
| F4 | 250–300 Tiere | GESCHÄTZT | Methode + Stand ergänzen |
| F5 | 13+ Versorgungsstationen | GESCHÄTZT | Stand prüfen, Positionen nicht veröffentlichen |
| F6 | 32 Rechnungen / 3.954,70 € / ~1.000 €/Monat | VERIFIZIERT (prüfen) | Zeitraum, Brutto/Netto, Vollständigkeit bestätigen |
| F7 | Murka e. V., AG Bochum VR 4939, Gemeinnützigkeit | VERIFIZIERT (prüfen) | Aktuellen Freistellungsbescheid bestätigen |
| F8 | Bankverbindung + Zweckbindung | OFFEN | Murka-Katzenhilfe e. V. |
| F9 | Margo-Statement (mehrfach reserviert) | OFFEN | Margo |
| F10 | Farm-Fotos für reservierte Bereiche | OFFEN | Margo (Freigabe) |
| F11 | Impressumspflichtige Angaben | OFFEN | Verantwortlicher |

---

## 5. Abweichungen vom Auftrag — meine Entscheidungen

Der Auftrag 3.0 ist in mehreren Punkten belastbarer als mein Entwurf 2.0. Ich übernehme ihn und korrigiere mich:

**A1 · Care Center wird zurückgestuft — Auftrag hat recht.**
Ich hatte die Care-Center-Roadmap zum „Herzstück" gemacht. Der Auftrag verbietet die Darstellung als beschlossenes Bauprojekt ohne geklärte Machbarkeit, Genehmigung und Finanzierung. Das ist die richtige Entscheidung: Eine Stiftung, die Genehmigungen nachfragt und keine findet, verliert Vertrauen dauerhaft. Care Center wird als **Option mit Bedingungen** dargestellt, Vollausbau erst in Phase 4.

**A2 · Gewinn-Frame bleibt, aber untergeordnet — Auftrag hat recht.**
Der Auftrag stellt klar: Tierwohl und Margos Entlastung zuerst, Nutzen für Helfende als *ergänzende* Ebene. Das ist die stärkere Position. Wer den Eigennutzen an die erste Stelle setzt, wirkt bei Stiftungen unseriös. Die Gewinn-Matrix bleibt — als zweite Ebene auf `mitmachen.html`, nicht als Leitbotschaft.

**A3 · Schulklassen- und Touristenformate: bewusster Aufschub — hier weiche ich von deiner Remarke ab.**
Du hattest Schulklassen und Touristen ausdrücklich gewünscht, der Auftrag schliesst sie ohne geklärte Betreuung, Sicherheit und Kapazität aus. **Ich folge dem Auftrag**, und zwar aus Sachgründen: Minderjährige und Laien auf einem Gelände mit ~250 teils scheuen oder kranken Tieren berühren Aufsichtspflicht, Haftung, Tollwut-/Bissrisiko und Tierstress. Ohne geklärte Aufsicht ist das ein reales Risiko für Kinder *und* Tiere — und ein einziger Zwischenfall würde die Initiative schwer beschädigen.
*Das ist kein Nein, sondern eine Reihenfolge:* Beides bleibt als Phase-3-Pilot vorgesehen, sobald Betreuungskapazität, Versicherung und Ablauf geklärt sind. Bis dahin wird nichts angekündigt, was noch nicht getragen werden kann. **Diese Entscheidung liegt bei dir — ich lege sie offen vor, statt sie still zu treffen.**

**A4 · Navigation: ich übernehme die Benennung des Auftrags.**
Statt meiner Fassung („Das Projekt · Katzen · Mitmachen · Fördern · Transparenz") gilt: **Unsere Arbeit · Katzen · Mitmachen · Fördern · Wirkung & Transparenz** + globaler CTA „Unterstützen". „Unsere Arbeit" ist verständlicher als „Das Projekt", und der Unterstützen-Hub fängt Unentschlossene sauber ab.

**A5 · Redirects: technische Anpassung nötig.**
GitHub Pages (CNAME vorhanden) kann keine serverseitigen 301-Weiterleitungen. Ich setze daher gemäss Auftrag 12.2 Redirect-Stubs mit Canonical, Meta-Refresh, JS-Fallback und sichtbarem Link ein.

---

## 6. Risiken

- **R1:** Ohne F1–F3 bleiben zentrale Module von `foerdern.html` ausgeblendet — die Seite verliert Argumentationskraft. Höchste inhaltliche Priorität.
- **R2:** Ohne F10 (Farm-Fotos) bleiben mehrere „Bereich reserviert"-Blöcke. Notfalls Bildbereiche ganz weglassen statt leer zeigen.
- **R3:** Umbenennungen (`ansatz` → `unsere-arbeit`, `veterinaerkosten` → `wirkung-transparenz`) kosten kurzfristig Suchmaschinen-Sichtbarkeit. Redirects mindern das; unvermeidbar.
- **R4:** Lokale Fonts/Tailwind-Build ändern die Deployment-Logik. Beim reinen statischen Setup ist ein kompiliertes CSS nötig.

---

## 7. Nächster Arbeitsschritt

**Schritt 1 — Fundament** (nach deiner Freigabe):
1. Sofortmassnahmen Sicherheit: Plus Code entfernen (B1), sichtbare Platzhalter ausblenden (B3).
2. Design-Tokens und Typografie konsolidieren.
3. Semantischer Header mit zugänglicher Desktop- und Mobile-Navigation (Fokusbindung, Escape, Schliessen-Button), Skip-Link, `aria-current`, einheitlicher Footer.
4. Wiederverwendbare Grundkomponenten und Statussystem (VERIFIZIERT/GESCHÄTZT/OFFEN mit Ausblendregel).
5. Globale Metadaten-Basis (Canonical, OG, `lang`, Sitemap, robots).

Erst danach Schritt 2 (Kernseiten). Keine Produktivschaltung ohne ausdrückliche Freigabe.
