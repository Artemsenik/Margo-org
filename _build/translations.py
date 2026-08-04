#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Übersetzungswörterbücher. Schlüssel = exakter deutscher Textabschnitt.
Reihenfolge ist wichtig: längere Zeichenketten zuerst ersetzen,
damit Teilstrings nicht vorzeitig getroffen werden.
"""

# ---------------------------------------------------------------- gemeinsam
COMMON_EN = {
    # Navigation & Rahmen
    "Zum Inhalt springen": "Skip to content",
    "Unsere Arbeit": "Our work",
    "Wirkung &amp; Transparenz": "Impact &amp; transparency",
    "Wirkung & Transparenz": "Impact &amp; transparency",
    "Mitmachen": "Get involved",
    "Unterstützen": "Support us",
    "Menü öffnen": "Open menu",
    "Katzen": "Cats",
    "Fördern": "Donate",
    "Hauptnavigation": "Main navigation",

    # Footer
    "Orientierung": "Overview",
    "Vertiefung": "Explore further",
    "Kontakt": "Contact",
    "Rechtliches": "Legal",
    "Versorgungsroute": "Care route",
    "Partner": "Partners",
    "Offene Rollen": "Open roles",
    "Impressum": "Legal notice",
    "Datenschutz": "Privacy policy",
    "Region Artemida/Athen, Griechenland": "Artemida / Athens region, Greece",
    "Antwort in der Regel innerhalb von 24 Stunden": "We usually reply within 24 hours",
    "Zuletzt aktualisiert: August 2026": "Last updated: August 2026",
    "Key facts &amp; overview": "Key facts &amp; overview",

    # Statusabzeichen
    "Verifiziert": "Verified",
    "Schätzung": "Estimate",
}

COMMON_EL = {
    "Zum Inhalt springen": "Μετάβαση στο περιεχόμενο",
    "Unsere Arbeit": "Το έργο μας",
    "Wirkung &amp; Transparenz": "Αντίκτυπος &amp; διαφάνεια",
    "Wirkung & Transparenz": "Αντίκτυπος &amp; διαφάνεια",
    "Mitmachen": "Συμμετοχή",
    "Unterstützen": "Στήριξη",
    "Menü öffnen": "Άνοιγμα μενού",
    "Katzen": "Γάτες",
    "Fördern": "Δωρεές",
    "Hauptnavigation": "Κύρια πλοήγηση",

    "Orientierung": "Προσανατολισμός",
    "Vertiefung": "Περισσότερα",
    "Kontakt": "Επικοινωνία",
    "Rechtliches": "Νομικά",
    "Versorgungsroute": "Διαδρομή φροντίδας",
    "Partner": "Συνεργάτες",
    "Offene Rollen": "Ανοιχτοί ρόλοι",
    "Impressum": "Στοιχεία ταυτότητας",
    "Datenschutz": "Πολιτική απορρήτου",
    "Region Artemida/Athen, Griechenland": "Περιοχή Αρτέμιδας / Αθήνας, Ελλάδα",
    "Antwort in der Regel innerhalb von 24 Stunden": "Απαντάμε συνήθως εντός 24 ωρών",
    "Zuletzt aktualisiert: August 2026": "Τελευταία ενημέρωση: Αύγουστος 2026",
    "Key facts &amp; overview": "Key facts &amp; overview",

    "Verifiziert": "Επιβεβαιωμένο",
    "Schätzung": "Εκτίμηση",
}

# ---------------------------------------------------------------- Startseite
INDEX_EN = {
    "Margo Animal Care | Tierhilfe in Artemida":
        "Margo Animal Care | Animal care in Artemida",
    "Margo versorgt rund um Artemida täglich Tiere. Die Initiative organisiert Unterstützung, dokumentiert Kosten und macht die Arbeit langfristig tragfähiger.":
        "Margo cares for animals around Artemida every single day. The initiative organises support, documents costs and makes the work sustainable in the long term.",

    "Margo Animal Care Initiative · Region Artemida, Griechenland":
        "Margo Animal Care Initiative · Artemida region, Greece",
    "Damit Margos Hilfe": "So Margo’s care can",
    "bleibt": "continue",
    "Margo versorgt rund um Artemida täglich eine grosse Zahl von Tieren.\n          Wir organisieren Unterstützung, dokumentieren Kosten und verteilen Aufgaben auf mehrere\n          Schultern — damit diese Arbeit nicht dauerhaft an einer Person hängt.":
        "Margo cares for a large number of animals around Artemida every day. We organise support,\n          document costs and share the workload across more shoulders — so that this work no longer\n          rests permanently on one person.",
    "Aktuell unterstützen": "Support this work",
    "Katzen kennenlernen": "Meet the cats",
    "Versorgung": "Daily care",
    "Tierärztliche Behandlung": "Veterinary treatment",
    "Kastration": "Neutering",
    "Vermittlung": "Rehoming",
    "Margo mit einer der von ihr versorgten Katzen":
        "Margo with one of the cats in her care",
    "Margo bei der täglichen Versorgung in der Region Artemida.":
        "Margo during her daily care round in the Artemida region.",

    "Belegter Stand": "Documented status",
    "Was dokumentiert ist": "What is documented",
    "Wir veröffentlichen nur Angaben, die belegt oder ausdrücklich als\n        Schätzung gekennzeichnet sind. Zu jeder Zahl gehören Definition und Zeitraum.":
        "We publish only figures that are documented or explicitly marked as an estimate.\n        Every number comes with a definition and a time period.",
    "Tierärztliche Kosten": "Veterinary costs",
    "Summe inklusive Mehrwertsteuer, aus 32 Einzelrechnungen.\n            Zeitraum 23.&nbsp;März bis 20.&nbsp;Juli 2026.":
        "Total including VAT, from 32 individual invoices.\n            Period 23&nbsp;March to 20&nbsp;July 2026.",
    "Vollständige Auswertung": "Full breakdown",
    "Tierarztrechnungen": "Veterinary invoices",
    "Abgerechnete Einzelbelege im selben Zeitraum, durchschnittlich rund\n            1.000&nbsp;€ pro Monat.":
        "Individual invoices settled in the same period, averaging around\n            €1,000 per month.",
    "Woraus die Kosten entstehen": "Where the costs come from",
    "Regelmässig versorgte Tiere": "Animals cared for regularly",
    "Näherung auf Basis der bekannten Versorgungsstellen, Stand 2026.\n            Eine exakte Zählung ist bei frei lebenden Tieren nicht möglich.":
        "An approximation based on the known care locations, as of 2026.\n            An exact count is not possible with free-living animals.",
    "Wie wir arbeiten": "How we work",
    "Erfasste Versorgungsstellen": "Recorded care locations",
    "Farm, private Versorgungsorte und Futterkolonien in der Region.\n            Genaue Standorte werden zum Schutz der Tiere nicht veröffentlicht.":
        "The farm, private care locations and feeding colonies in the region.\n            Exact locations are not published, to protect the animals.",
    "Die Versorgungsroute": "The care route",

    "Drei direkte Wege": "Three direct ways",
    "Wo Sie ansetzen können": "Where you can start",
    "Eine Katze kennenlernen": "Meet a cat",
    "Lernen Sie Katzen mit aktuellem Status, ehrlicher Beschreibung und transparentem\n            Vermittlungsweg kennen.":
        "Get to know cats with their current status, an honest description and a transparent\n            rehoming process.",
    "Katzen ansehen": "View the cats",
    "Zeit oder Können beitragen": "Contribute time or skills",
    "Übernehmen Sie eine klar begrenzte Aufgabe vor Ort oder remote — mit realistischem\n            Aufwand und festem Ansprechpartner.":
        "Take on a clearly defined task on site or remotely — with a realistic time commitment\n            and a named contact person.",
    "Offene Rollen prüfen": "Review open roles",
    "Versorgung finanzieren": "Fund the care",
    "Unterstützen Sie tierärztliche Behandlung, Kastration, Futter oder ein klar\n            beschriebenes Vorhaben.":
        "Support veterinary treatment, neutering, food or a clearly described project.",
    "Unterstützung wählen": "Choose how to help",

    "Wie es begann": "How it began",
    "Wie aus persönlicher Verantwortung eine gemeinsame Aufgabe wird.":
        "How personal responsibility becomes a shared task.",
    "Vor Jahren begann Margo, einzelne Strassenkatzen rund um Artemida zu versorgen. Aus\n          wenigen Tieren wurden viele. Ein Brand zerstörte das Strandcafé, das sie betrieb — die\n          Tiere blieben, und mit ihnen die tägliche Verantwortung.":
        "Years ago Margo began caring for a few street cats around Artemida. A handful of animals\n          became many. A fire destroyed the beach café she ran — the animals remained, and with them\n          the daily responsibility.",
    "Heute fährt sie ihre Touren, organisiert Behandlungen und trägt\n          vieles selbst. Genau hier setzt die Initiative an: Wissen ordnen, Kosten offenlegen,\n          Aufgaben teilen.":
        "Today she drives her rounds, arranges treatments and carries much of it herself. This is\n          exactly where the initiative comes in: organising knowledge, disclosing costs, sharing tasks.",
    "Margos Geschichte ansehen": "Read Margo’s story",
    "Margo versorgt Katzen an einer Futterstelle": "Margo feeding cats at a feeding station",

    "Arbeitsbereiche": "Areas of work",
    "Was heute konkret geschieht": "What is happening right now",
    "Versorgung und Beobachtung": "Care and observation",
    "Regelmässige Versorgung und Beobachtung an mehreren Stellen in der Region.":
        "Regular feeding and monitoring at several locations across the region.",
    "Behandlung und Kastration": "Treatment and neutering",
    "Tierärztliche Abklärung, Behandlung und präventive Massnahmen nach fachlicher Entscheidung.":
        "Veterinary assessment, treatment and preventive measures based on professional judgement.",
    "Dokumentation und Vermittlung": "Documentation and rehoming",
    "Profile, Gesundheitsinformationen, Zuständigkeiten und verantwortungsvolle Vermittlungswege.":
        "Profiles, health information, clear responsibilities and responsible rehoming routes.",
    "Koordination und Entlastung": "Coordination and relief",
    "Aufgaben, Partner, Kosten und Fortschritt so organisieren, dass nicht alles an einer Person hängt.":
        "Organising tasks, partners, costs and progress so that not everything depends on one person.",

    "Die Route hinter der Fürsorge": "The route behind the care",
    "Eine dokumentarische Reise durch die Orte, an denen aus einzelnen Fütterungen eine\n            tägliche Verantwortung entsteht.":
        "A documentary journey through the places where individual feedings grow into a daily\n            responsibility.",
    "Route ansehen": "View the route",
    "Das mit Futter und Wasser beladene Fahrzeug vor einer Versorgungstour":
        "The vehicle loaded with food and water before a care round",

    "Wer mitträgt": "Who shares the load",
    "Margo trägt das nicht allein": "Margo does not carry this alone",
    "Ein eingetragener Partnerverein": "A registered partner association",
    "Murka-Katzenhilfe e.&nbsp;V. (Amtsgericht Bochum, VR&nbsp;4939) wickelt Spenden und\n              Vermittlungen nach Deutschland ab.":
        "Murka-Katzenhilfe e.&nbsp;V. (Bochum Local Court, VR&nbsp;4939) handles donations and\n              rehoming to Germany.",
    "Zwei Tierarztpraxen": "Two veterinary practices",
    "Vets4life und OmniVET behandeln die Tiere zu vergünstigten Konditionen.":
        "Vets4life and OmniVET treat the animals at reduced rates.",
    "Vier Futtergeschäfte": "Four pet food shops",
    "Pet City, Pet Shop Manos, Pet Point und Dogit gewähren Vergünstigungen auf Futter.":
        "Pet City, Pet Shop Manos, Pet Point and Dogit grant discounts on food.",
    "Eine Windsurfing-Schule": "A windsurfing school",
    "Trägt finanziell bei und ist Zuhause für einen Teil der versorgten Katzen.":
        "Contributes financially and is home to some of the cats in care.",
    "Alle Partner mit Kontaktangaben finden Sie auf der":
        "You will find all partners with contact details on the",
    "Partnerseite": "partners page",
    ". Wie Mittel eingesetzt werden, zeigt": ". How funds are used is shown under",
    "Wie Mittel eingesetzt werden, zeigt": "How funds are used is shown under",
}

INDEX_EL = {
    "Margo Animal Care | Tierhilfe in Artemida":
        "Margo Animal Care | Φροντίδα ζώων στην Αρτέμιδα",
    "Margo versorgt rund um Artemida täglich Tiere. Die Initiative organisiert Unterstützung, dokumentiert Kosten und macht die Arbeit langfristig tragfähiger.":
        "Η Margo φροντίζει καθημερινά ζώα στην περιοχή της Αρτέμιδας. Η πρωτοβουλία οργανώνει τη στήριξη, τεκμηριώνει τα έξοδα και κάνει το έργο βιώσιμο μακροπρόθεσμα.",

    "Margo Animal Care Initiative · Region Artemida, Griechenland":
        "Margo Animal Care Initiative · Περιοχή Αρτέμιδας, Ελλάδα",
    "Damit Margos Hilfe": "Για να συνεχιστεί η φροντίδα",
    "bleibt": "της Margo",
    "Margo versorgt rund um Artemida täglich eine grosse Zahl von Tieren.\n          Wir organisieren Unterstützung, dokumentieren Kosten und verteilen Aufgaben auf mehrere\n          Schultern — damit diese Arbeit nicht dauerhaft an einer Person hängt.":
        "Η Margo φροντίζει καθημερινά μεγάλο αριθμό ζώων γύρω από την Αρτέμιδα. Οργανώνουμε τη στήριξη,\n          τεκμηριώνουμε τα έξοδα και μοιράζουμε τις εργασίες σε περισσότερους ώμους — ώστε αυτό το έργο\n          να μη στηρίζεται μόνιμα σε ένα άτομο.",
    "Aktuell unterstützen": "Στηρίξτε το έργο",
    "Katzen kennenlernen": "Γνωρίστε τις γάτες",
    "Versorgung": "Καθημερινή φροντίδα",
    "Tierärztliche Behandlung": "Κτηνιατρική περίθαλψη",
    "Kastration": "Στείρωση",
    "Vermittlung": "Υιοθεσία",
    "Margo mit einer der von ihr versorgten Katzen":
        "Η Margo με μία από τις γάτες που φροντίζει",
    "Margo bei der täglichen Versorgung in der Region Artemida.":
        "Η Margo κατά την καθημερινή της φροντίδα στην περιοχή της Αρτέμιδας.",

    "Belegter Stand": "Τεκμηριωμένα στοιχεία",
    "Was dokumentiert ist": "Τι είναι τεκμηριωμένο",
    "Wir veröffentlichen nur Angaben, die belegt oder ausdrücklich als\n        Schätzung gekennzeichnet sind. Zu jeder Zahl gehören Definition und Zeitraum.":
        "Δημοσιεύουμε μόνο στοιχεία που είναι τεκμηριωμένα ή επισημαίνονται ρητά ως εκτίμηση.\n        Κάθε αριθμός συνοδεύεται από ορισμό και χρονική περίοδο.",
    "Tierärztliche Kosten": "Κτηνιατρικά έξοδα",
    "Summe inklusive Mehrwertsteuer, aus 32 Einzelrechnungen.\n            Zeitraum 23.&nbsp;März bis 20.&nbsp;Juli 2026.":
        "Σύνολο με ΦΠΑ, από 32 επιμέρους τιμολόγια.\n            Περίοδος 23&nbsp;Μαρτίου έως 20&nbsp;Ιουλίου 2026.",
    "Vollständige Auswertung": "Πλήρης ανάλυση",
    "Tierarztrechnungen": "Κτηνιατρικά τιμολόγια",
    "Abgerechnete Einzelbelege im selben Zeitraum, durchschnittlich rund\n            1.000&nbsp;€ pro Monat.":
        "Επιμέρους παραστατικά της ίδιας περιόδου, κατά μέσο όρο περίπου\n            1.000&nbsp;€ τον μήνα.",
    "Woraus die Kosten entstehen": "Από πού προκύπτουν τα έξοδα",
    "Regelmässig versorgte Tiere": "Ζώα σε τακτική φροντίδα",
    "Näherung auf Basis der bekannten Versorgungsstellen, Stand 2026.\n            Eine exakte Zählung ist bei frei lebenden Tieren nicht möglich.":
        "Προσέγγιση βάσει των γνωστών σημείων φροντίδας, στοιχεία 2026.\n            Ακριβής καταμέτρηση δεν είναι εφικτή σε ελεύθερα ζώα.",
    "Wie wir arbeiten": "Πώς εργαζόμαστε",
    "Erfasste Versorgungsstellen": "Καταγεγραμμένα σημεία φροντίδας",
    "Farm, private Versorgungsorte und Futterkolonien in der Region.\n            Genaue Standorte werden zum Schutz der Tiere nicht veröffentlicht.":
        "Η φάρμα, ιδιωτικά σημεία φροντίδας και αποικίες σίτισης στην περιοχή.\n            Οι ακριβείς τοποθεσίες δεν δημοσιεύονται, για την προστασία των ζώων.",
    "Die Versorgungsroute": "Η διαδρομή φροντίδας",

    "Drei direkte Wege": "Τρεις άμεσοι τρόποι",
    "Wo Sie ansetzen können": "Από πού μπορείτε να ξεκινήσετε",
    "Eine Katze kennenlernen": "Γνωρίστε μια γάτα",
    "Lernen Sie Katzen mit aktuellem Status, ehrlicher Beschreibung und transparentem\n            Vermittlungsweg kennen.":
        "Γνωρίστε γάτες με την τρέχουσα κατάστασή τους, ειλικρινή περιγραφή και διαφανή\n            διαδικασία υιοθεσίας.",
    "Katzen ansehen": "Δείτε τις γάτες",
    "Zeit oder Können beitragen": "Προσφέρετε χρόνο ή δεξιότητες",
    "Übernehmen Sie eine klar begrenzte Aufgabe vor Ort oder remote — mit realistischem\n            Aufwand und festem Ansprechpartner.":
        "Αναλάβετε μια σαφώς οριοθετημένη εργασία επιτόπου ή εξ αποστάσεως — με ρεαλιστικό\n            φόρτο και συγκεκριμένο υπεύθυνο επικοινωνίας.",
    "Offene Rollen prüfen": "Δείτε τους ανοιχτούς ρόλους",
    "Versorgung finanzieren": "Χρηματοδοτήστε τη φροντίδα",
    "Unterstützen Sie tierärztliche Behandlung, Kastration, Futter oder ein klar\n            beschriebenes Vorhaben.":
        "Στηρίξτε κτηνιατρική περίθαλψη, στειρώσεις, τροφή ή ένα σαφώς περιγεγραμμένο έργο.",
    "Unterstützung wählen": "Επιλέξτε πώς θα βοηθήσετε",

    "Wie es begann": "Πώς ξεκίνησε",
    "Wie aus persönlicher Verantwortung eine gemeinsame Aufgabe wird.":
        "Πώς μια προσωπική ευθύνη γίνεται κοινό έργο.",
    "Vor Jahren begann Margo, einzelne Strassenkatzen rund um Artemida zu versorgen. Aus\n          wenigen Tieren wurden viele. Ein Brand zerstörte das Strandcafé, das sie betrieb — die\n          Tiere blieben, und mit ihnen die tägliche Verantwortung.":
        "Πριν από χρόνια η Margo άρχισε να φροντίζει μερικές αδέσποτες γάτες γύρω από την Αρτέμιδα.\n          Από λίγα ζώα έγιναν πολλά. Μια πυρκαγιά κατέστρεψε το beach café που είχε — τα ζώα έμειναν,\n          και μαζί τους η καθημερινή ευθύνη.",
    "Heute fährt sie ihre Touren, organisiert Behandlungen und trägt\n          vieles selbst. Genau hier setzt die Initiative an: Wissen ordnen, Kosten offenlegen,\n          Aufgaben teilen.":
        "Σήμερα κάνει τις διαδρομές της, οργανώνει θεραπείες και επωμίζεται πολλά η ίδια. Ακριβώς εδώ\n          παρεμβαίνει η πρωτοβουλία: να οργανώσει τη γνώση, να δημοσιοποιήσει τα έξοδα, να μοιράσει τα καθήκοντα.",
    "Margos Geschichte ansehen": "Δείτε την ιστορία της Margo",
    "Margo versorgt Katzen an einer Futterstelle": "Η Margo ταΐζει γάτες σε σημείο σίτισης",

    "Arbeitsbereiche": "Τομείς εργασίας",
    "Was heute konkret geschieht": "Τι γίνεται σήμερα συγκεκριμένα",
    "Versorgung und Beobachtung": "Φροντίδα και παρακολούθηση",
    "Regelmässige Versorgung und Beobachtung an mehreren Stellen in der Region.":
        "Τακτική σίτιση και παρακολούθηση σε πολλά σημεία της περιοχής.",
    "Behandlung und Kastration": "Περίθαλψη και στείρωση",
    "Tierärztliche Abklärung, Behandlung und präventive Massnahmen nach fachlicher Entscheidung.":
        "Κτηνιατρική εκτίμηση, θεραπεία και προληπτικά μέτρα βάσει επαγγελματικής κρίσης.",
    "Dokumentation und Vermittlung": "Τεκμηρίωση και υιοθεσίες",
    "Profile, Gesundheitsinformationen, Zuständigkeiten und verantwortungsvolle Vermittlungswege.":
        "Προφίλ, στοιχεία υγείας, σαφείς αρμοδιότητες και υπεύθυνες διαδικασίες υιοθεσίας.",
    "Koordination und Entlastung": "Συντονισμός και ανακούφιση",
    "Aufgaben, Partner, Kosten und Fortschritt so organisieren, dass nicht alles an einer Person hängt.":
        "Οργάνωση εργασιών, συνεργατών, εξόδων και προόδου, ώστε να μην εξαρτώνται όλα από ένα άτομο.",

    "Die Route hinter der Fürsorge": "Η διαδρομή πίσω από τη φροντίδα",
    "Eine dokumentarische Reise durch die Orte, an denen aus einzelnen Fütterungen eine\n            tägliche Verantwortung entsteht.":
        "Ένα ντοκιμαντέρ-ταξίδι στα σημεία όπου μεμονωμένες σιτίσεις γίνονται καθημερινή ευθύνη.",
    "Route ansehen": "Δείτε τη διαδρομή",
    "Das mit Futter und Wasser beladene Fahrzeug vor einer Versorgungstour":
        "Το όχημα φορτωμένο με τροφή και νερό πριν από μια διαδρομή φροντίδας",

    "Wer mitträgt": "Ποιοι στηρίζουν",
    "Margo trägt das nicht allein": "Η Margo δεν το κάνει μόνη της",
    "Ein eingetragener Partnerverein": "Ένας εγγεγραμμένος συνεργαζόμενος σύλλογος",
    "Murka-Katzenhilfe e.&nbsp;V. (Amtsgericht Bochum, VR&nbsp;4939) wickelt Spenden und\n              Vermittlungen nach Deutschland ab.":
        "Ο Murka-Katzenhilfe e.&nbsp;V. (Πρωτοδικείο Bochum, VR&nbsp;4939) διαχειρίζεται τις δωρεές και\n              τις υιοθεσίες προς τη Γερμανία.",
    "Zwei Tierarztpraxen": "Δύο κτηνιατρεία",
    "Vets4life und OmniVET behandeln die Tiere zu vergünstigten Konditionen.":
        "Τα Vets4life και OmniVET περιθάλπουν τα ζώα με μειωμένες χρεώσεις.",
    "Vier Futtergeschäfte": "Τέσσερα καταστήματα τροφών",
    "Pet City, Pet Shop Manos, Pet Point und Dogit gewähren Vergünstigungen auf Futter.":
        "Τα Pet City, Pet Shop Manos, Pet Point και Dogit προσφέρουν εκπτώσεις σε τροφές.",
    "Eine Windsurfing-Schule": "Μια σχολή windsurfing",
    "Trägt finanziell bei und ist Zuhause für einen Teil der versorgten Katzen.":
        "Συνεισφέρει οικονομικά και φιλοξενεί μέρος των γατών που φροντίζονται.",
    "Alle Partner mit Kontaktangaben finden Sie auf der":
        "Όλους τους συνεργάτες με στοιχεία επικοινωνίας θα βρείτε στη",
    "Partnerseite": "σελίδα συνεργατών",
    ". Wie Mittel eingesetzt werden, zeigt": ". Πώς αξιοποιούνται οι πόροι φαίνεται στο",
    "Wie Mittel eingesetzt werden, zeigt": "Πώς αξιοποιούνται οι πόροι φαίνεται στο",
}
