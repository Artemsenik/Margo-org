#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Geteilte Strukturtexte und Namens-Schablonen der Katzenprofile."""

# ---------------------------------------------------------- Schablonen ({N} = Katzenname)
TPL_EN = {
    "Interesse an {N}": "Interested in {N}",
    "{N} auf einen Blick": "{N} at a glance",
    "So ist {N}": "What {N} is like",
    "{N} in Bildern": "{N} in pictures",
    "Könnte {N} zu": "Could {N} fit into",
    "{N}s ideales Zuhause": "{N}’s ideal home",
    "{N}' ideales Zuhause": "{N}’ ideal home",
    "{N} ist geimpft.": "{N} is vaccinated.",
    "{N} ist kastriert.": "{N} is neutered.",
    "{N} ist sterilisiert.": "{N} is spayed.",
    "Keine Bedingungsliste – eine Beschreibung, worin {N} nach unseren Beobachtungen aufblüht.":
        "Not a list of conditions – a description of where {N} flourishes, according to our observations.",
    "Kein Anforderungskatalog – eher eine Beschreibung dessen, worin {N} nach unseren Beobachtungen aufblüht.":
        "Not a catalogue of requirements – rather a description of where {N} flourishes, according to our observations.",
    "Keine Liste von Bedingungen – eher eine Beschreibung, worin {N} nach unseren Beobachtungen aufblüht.":
        "Not a list of conditions – rather a description of where {N} flourishes, according to our observations.",
    "Keine Liste von Anforderungen – eher eine Beschreibung, worin {N} nach unseren Beobachtungen aufblüht.":
        "Not a list of requirements – rather a description of where {N} flourishes, according to our observations.",
    "Die Margo Animal Care Initiative stellt {N} und ihre Geschichte vor. Bewerbung, Prüfung und Vermittlung erfolgen über Murka-Katzenhilfe e.&nbsp;V.":
        "The Margo Animal Care Initiative introduces {N} and her story. Application, vetting and rehoming are handled by Murka-Katzenhilfe e.&nbsp;V.",
    "Die Margo Animal Care Initiative stellt {N} und seine Geschichte vor. Bewerbung, Prüfung und Vermittlung erfolgen über Murka-Katzenhilfe e.&nbsp;V.":
        "The Margo Animal Care Initiative introduces {N} and his story. Application, vetting and rehoming are handled by Murka-Katzenhilfe e.&nbsp;V.",
    "Wenn du dir vorstellen kannst, {N} ein Zuhause zu geben, führt der nächste Schritt zu Murka-Katzenhilfe e.&nbsp;V. Dort wird gemeinsam geprüft, ob es für euch beide passt.":
        "If you can imagine giving {N} a home, the next step leads to Murka-Katzenhilfe e.&nbsp;V. Together you will look at whether it is right for both of you.",
    "Wenn du dir vorstellen kannst, {N} ein ruhiges Zuhause zu geben, führt der nächste Schritt zu Murka-Katzenhilfe e.&nbsp;V. Dort wird gemeinsam geprüft, ob es für euch beide passt.":
        "If you can imagine giving {N} a quiet home, the next step leads to Murka-Katzenhilfe e.&nbsp;V. Together you will look at whether it is right for both of you.",
    "Wenn du dir vorstellen kannst, {N} ein ruhiges Zuhause zu geben, führt der nächste Schritt zu Murka-Katzenhilfe e.&nbsp;V. Dort wird gemeinsam mit dir geprüft, ob es für euch beide passt.":
        "If you can imagine giving {N} a quiet home, the next step leads to Murka-Katzenhilfe e.&nbsp;V. Together with you they will look at whether it is right for both of you.",
    "Die Haltungsform wird gemeinsam mit Murka-Katzenhilfe e.&nbsp;V. entschieden – passend zu {N} und zur konkreten Wohnsituation.":
        "The way of keeping is decided together with Murka-Katzenhilfe e.&nbsp;V. – suited to {N} and to the actual living situation.",
}

TPL_EL = {
    "Interesse an {N}": "Ενδιαφέρομαι για {N}",
    "{N} auf einen Blick": "{N} με μια ματιά",
    "So ist {N}": "Έτσι είναι η/ο {N}",
    "{N} in Bildern": "{N} σε εικόνες",
    "Könnte {N} zu": "Θα ταίριαζε η/ο {N} στη",
    "{N}s ideales Zuhause": "Το ιδανικό σπίτι για {N}",
    "{N}' ideales Zuhause": "Το ιδανικό σπίτι για {N}",
    "{N} ist geimpft.": "Η/ο {N} είναι εμβολιασμένη/ος.",
    "{N} ist kastriert.": "Ο {N} είναι στειρωμένος.",
    "{N} ist sterilisiert.": "Η {N} είναι στειρωμένη.",
    "Keine Bedingungsliste – eine Beschreibung, worin {N} nach unseren Beobachtungen aufblüht.":
        "Όχι λίστα προϋποθέσεων – μια περιγραφή του πού ανθίζει η/ο {N}, σύμφωνα με τις παρατηρήσεις μας.",
    "Kein Anforderungskatalog – eher eine Beschreibung dessen, worin {N} nach unseren Beobachtungen aufblüht.":
        "Όχι κατάλογος απαιτήσεων – μάλλον μια περιγραφή του πού ανθίζει η/ο {N}, σύμφωνα με τις παρατηρήσεις μας.",
    "Keine Liste von Bedingungen – eher eine Beschreibung, worin {N} nach unseren Beobachtungen aufblüht.":
        "Όχι λίστα προϋποθέσεων – μάλλον μια περιγραφή του πού ανθίζει η/ο {N}, σύμφωνα με τις παρατηρήσεις μας.",
    "Keine Liste von Anforderungen – eher eine Beschreibung, worin {N} nach unseren Beobachtungen aufblüht.":
        "Όχι λίστα απαιτήσεων – μάλλον μια περιγραφή του πού ανθίζει η/ο {N}, σύμφωνα με τις παρατηρήσεις μας.",
    "Die Margo Animal Care Initiative stellt {N} und ihre Geschichte vor. Bewerbung, Prüfung und Vermittlung erfolgen über Murka-Katzenhilfe e.&nbsp;V.":
        "Η Margo Animal Care Initiative παρουσιάζει την {N} και την ιστορία της. Η αίτηση, ο έλεγχος και η υιοθεσία γίνονται μέσω του Murka-Katzenhilfe e.&nbsp;V.",
    "Die Margo Animal Care Initiative stellt {N} und seine Geschichte vor. Bewerbung, Prüfung und Vermittlung erfolgen über Murka-Katzenhilfe e.&nbsp;V.":
        "Η Margo Animal Care Initiative παρουσιάζει τον {N} και την ιστορία του. Η αίτηση, ο έλεγχος και η υιοθεσία γίνονται μέσω του Murka-Katzenhilfe e.&nbsp;V.",
    "Wenn du dir vorstellen kannst, {N} ein Zuhause zu geben, führt der nächste Schritt zu Murka-Katzenhilfe e.&nbsp;V. Dort wird gemeinsam geprüft, ob es für euch beide passt.":
        "Αν μπορείς να φανταστείς να δώσεις στη/στον {N} ένα σπίτι, το επόμενο βήμα οδηγεί στον Murka-Katzenhilfe e.&nbsp;V. Εκεί εξετάζεται από κοινού αν ταιριάζει και για τους δυο σας.",
    "Wenn du dir vorstellen kannst, {N} ein ruhiges Zuhause zu geben, führt der nächste Schritt zu Murka-Katzenhilfe e.&nbsp;V. Dort wird gemeinsam geprüft, ob es für euch beide passt.":
        "Αν μπορείς να φανταστείς να δώσεις στη/στον {N} ένα ήσυχο σπίτι, το επόμενο βήμα οδηγεί στον Murka-Katzenhilfe e.&nbsp;V. Εκεί εξετάζεται από κοινού αν ταιριάζει και για τους δυο σας.",
    "Wenn du dir vorstellen kannst, {N} ein ruhiges Zuhause zu geben, führt der nächste Schritt zu Murka-Katzenhilfe e.&nbsp;V. Dort wird gemeinsam mit dir geprüft, ob es für euch beide passt.":
        "Αν μπορείς να φανταστείς να δώσεις στη/στον {N} ένα ήσυχο σπίτι, το επόμενο βήμα οδηγεί στον Murka-Katzenhilfe e.&nbsp;V. Εκεί θα εξεταστεί μαζί σου αν ταιριάζει και για τους δυο σας.",
    "Die Haltungsform wird gemeinsam mit Murka-Katzenhilfe e.&nbsp;V. entschieden – passend zu {N} und zur konkreten Wohnsituation.":
        "Ο τρόπος διαβίωσης αποφασίζεται από κοινού με τον Murka-Katzenhilfe e.&nbsp;V. – ανάλογα με τη/τον {N} και τις συγκεκριμένες συνθήκες κατοικίας.",
}

# ---------------------------------------------------------- geteilte Strukturtexte
SHARED_EN = {
    "Gesicherter Balkon willkommen": "Secured balcony welcome",
    "Region Athen, Griechenland": "Athens region, Greece",
    "Region Artemida, Griechenland": "Artemida region, Greece",
    "Vermittelt wird in liebevolle Wohnungshaltung oder in ein Zuhause mit gesichertem Freigang. In entsprechend geeigneter und sicherer Umgebung kann auch Freigang ermöglicht werden.":
        "Rehoming is into a loving indoor home or a home with secured outdoor access. In a suitably safe environment, outdoor access can also be made possible.",
    "Alle Angaben geben den Stand wieder, der uns zum Zeitpunkt der letzten Aktualisierung bekannt war.":
        "All information reflects what was known to us at the time of the last update.",
    "Alle Fragen zu Ablauf, Schutzgebühr, Vorkontrolle und Übergabe beantwortet der Verein.":
        "All questions about the process, the adoption fee, the home check and the handover are answered by the association.",
    "Erfahrung mit Hunden": "Experience with dogs",
    "Erfahrung mit kleinen Hunden": "Experience with small dogs",
    "vorhanden": "yes",
    "unbekannt": "unknown",
    "weiblich · sucht ein Zuhause": "female · looking for a home",
    "Kater · sucht ein Zuhause": "male · looking for a home",
    "Kastriert/Sterilisiert": "Neutered/spayed",
    "Hunde": "Dogs",
    "Hunde möglich": "Dogs possible",
    "Ihr Wesen": "Her character",
    "Sein Wesen": "His character",
    "Was wir hier beschreiben, beruht auf den Beobachtungen aus ihrem Alltag – nicht auf Zusicherungen.":
        "What we describe here is based on observations from her everyday life – not on guarantees.",
    "Was wir hier beschreiben, beruht auf den Beobachtungen aus seinem Alltag – nicht auf Zusicherungen.":
        "What we describe here is based on observations from his everyday life – not on guarantees.",
    "Ihre Geschichte": "Her story",
    "Seine Geschichte": "His story",
    "Was zu ihr passt": "What suits her",
    "Was zu ihm passt": "What suits him",
    "Gesundheit": "Health",
    "Gesundheit und medizinischer Verlauf": "Health and medical history",
    "Diese Angaben halten wir bewusst getrennt von seiner Geschichte – sie sollen nüchtern nachvollziehbar sein.":
        "We deliberately keep this information separate from his story – it should be soberly verifiable.",
    "Diese Angaben halten wir bewusst getrennt von ihrer Geschichte – sie sollen nüchtern nachvollziehbar sein.":
        "We deliberately keep this information separate from her story – it should be soberly verifiable.",
    "Abschliessende medizinische Prüfung im Vermittlungsprozess.":
        "Final medical check during the rehoming process.",
    "Die abschliessende medizinische Prüfung erfolgt im Rahmen des Vermittlungsprozesses.":
        "The final medical check takes place as part of the rehoming process.",
    "Aufnahmen aus ihrem Alltag. Zum Vergrössern anklicken oder mit Enter öffnen.":
        "Images from her everyday life. Click to enlarge or open with Enter.",
    "Aufnahmen aus seinem Alltag. Zum Vergrössern anklicken oder mit Enter öffnen.":
        "Images from his everyday life. Click to enlarge or open with Enter.",
    "Alltagsaufnahmen aus seiner Versorgung. Zum Vergrössern anklicken – oder mit der Tastatur ansteuern und mit Enter öffnen.":
        "Everyday images from his care. Click to enlarge – or navigate with the keyboard and open with Enter.",
    "Letzte Aktualisierung: 21. Juli 2026": "Last updated: 21 July 2026",
    "Letzte Aktualisierung des Profils: 17. Juli 2026": "Profile last updated: 17 July 2026",
    "vor der Ausreise vorgesehen (FIV- und FeLV-Test).": "planned before departure (FIV and FeLV test).",
    "Ein FIV- und FeLV-Test wird vor der Ausreise durchgeführt.":
        "An FIV and FeLV test is carried out before departure.",
    "Andere Katzen möglich": "Other cats possible",
    "Gut mit anderen Katzen": "Good with other cats",
    "Friedlich mit Artgenossen": "Peaceful with other cats",
    "Verhalten mit Katzen": "Behaviour with cats",
    "geimpft": "vaccinated",
    "kastriert": "neutered",
    "sterilisiert": "spayed",
    "EKH-Mix": "domestic shorthair mix",
    "Wohnungshaltung oder gesicherter Freigang": "Indoor home or secured outdoor access",
    "Ruhige Atmosphäre": "A calm atmosphere",
    "Eigene Rückzugsorte": "Places of her own to retreat to",
    "Rückzugsorte": "Places to retreat",
    "Rückzug möglich": "Retreat possible",
    "Details werden bei Ausreise ergänzt.": "Details will be added at departure.",
    "ca. 2023": "approx. 2023",
    "Haltungsform nach Prüfung": "Keeping decided after review",
    "Menschen, die bleiben": "People who stay",
    "Ruhig und liebevoll": "Calm and loving",
    "Andere Katzen? Individuell": "Other cats? Case by case",
    "Wir machen bewusst keine Aussage über Befunde, die noch nicht vorliegen. Alle medizinischen Angaben geben den Stand wieder, der uns zum Zeitpunkt der letzten Aktualisierung bekannt war.":
        "We deliberately make no statement about findings that are not yet available. All medical information reflects the status known to us at the time of the last update.",
}

SHARED_EL = {
    "Gesicherter Balkon willkommen": "Ασφαλές μπαλκόνι ευπρόσδεκτο",
    "Region Athen, Griechenland": "Περιοχή Αθηνών, Ελλάδα",
    "Region Artemida, Griechenland": "Περιοχή Αρτέμιδας, Ελλάδα",
    "Vermittelt wird in liebevolle Wohnungshaltung oder in ein Zuhause mit gesichertem Freigang. In entsprechend geeigneter und sicherer Umgebung kann auch Freigang ermöglicht werden.":
        "Η υιοθεσία γίνεται σε στοργικό σπίτι εσωτερικού χώρου ή σε σπίτι με ασφαλή εξωτερική πρόσβαση. Σε κατάλληλο και ασφαλές περιβάλλον μπορεί να επιτραπεί και ελεύθερη έξοδος.",
    "Alle Angaben geben den Stand wieder, der uns zum Zeitpunkt der letzten Aktualisierung bekannt war.":
        "Όλα τα στοιχεία αποτυπώνουν όσα γνωρίζαμε κατά την τελευταία ενημέρωση.",
    "Alle Fragen zu Ablauf, Schutzgebühr, Vorkontrolle und Übergabe beantwortet der Verein.":
        "Όλες τις ερωτήσεις για τη διαδικασία, το τέλος υιοθεσίας, τον προέλεγχο και την παράδοση τις απαντά ο σύλλογος.",
    "Erfahrung mit Hunden": "Εμπειρία με σκύλους",
    "Erfahrung mit kleinen Hunden": "Εμπειρία με μικρούς σκύλους",
    "vorhanden": "ναι",
    "unbekannt": "άγνωστο",
    "weiblich · sucht ein Zuhause": "θηλυκό · αναζητά σπίτι",
    "Kater · sucht ein Zuhause": "αρσενικό · αναζητά σπίτι",
    "Kastriert/Sterilisiert": "Στειρωμένη/ος",
    "Hunde": "Σκύλοι",
    "Hunde möglich": "Σκύλοι πιθανοί",
    "Ihr Wesen": "Ο χαρακτήρας της",
    "Sein Wesen": "Ο χαρακτήρας του",
    "Was wir hier beschreiben, beruht auf den Beobachtungen aus ihrem Alltag – nicht auf Zusicherungen.":
        "Όσα περιγράφουμε εδώ βασίζονται σε παρατηρήσεις από την καθημερινότητά της – όχι σε εγγυήσεις.",
    "Was wir hier beschreiben, beruht auf den Beobachtungen aus seinem Alltag – nicht auf Zusicherungen.":
        "Όσα περιγράφουμε εδώ βασίζονται σε παρατηρήσεις από την καθημερινότητά του – όχι σε εγγυήσεις.",
    "Ihre Geschichte": "Η ιστορία της",
    "Seine Geschichte": "Η ιστορία του",
    "Was zu ihr passt": "Τι της ταιριάζει",
    "Was zu ihm passt": "Τι του ταιριάζει",
    "Gesundheit": "Υγεία",
    "Gesundheit und medizinischer Verlauf": "Υγεία και ιατρικό ιστορικό",
    "Diese Angaben halten wir bewusst getrennt von seiner Geschichte – sie sollen nüchtern nachvollziehbar sein.":
        "Αυτά τα στοιχεία τα κρατάμε σκόπιμα χωριστά από την ιστορία του – πρέπει να είναι νηφάλια και ελέγξιμα.",
    "Diese Angaben halten wir bewusst getrennt von ihrer Geschichte – sie sollen nüchtern nachvollziehbar sein.":
        "Αυτά τα στοιχεία τα κρατάμε σκόπιμα χωριστά από την ιστορία της – πρέπει να είναι νηφάλια και ελέγξιμα.",
    "Abschliessende medizinische Prüfung im Vermittlungsprozess.":
        "Τελικός ιατρικός έλεγχος κατά τη διαδικασία υιοθεσίας.",
    "Die abschliessende medizinische Prüfung erfolgt im Rahmen des Vermittlungsprozesses.":
        "Ο τελικός ιατρικός έλεγχος πραγματοποιείται στο πλαίσιο της διαδικασίας υιοθεσίας.",
    "Aufnahmen aus ihrem Alltag. Zum Vergrössern anklicken oder mit Enter öffnen.":
        "Εικόνες από την καθημερινότητά της. Κάντε κλικ για μεγέθυνση ή ανοίξτε με Enter.",
    "Aufnahmen aus seinem Alltag. Zum Vergrössern anklicken oder mit Enter öffnen.":
        "Εικόνες από την καθημερινότητά του. Κάντε κλικ για μεγέθυνση ή ανοίξτε με Enter.",
    "Alltagsaufnahmen aus seiner Versorgung. Zum Vergrössern anklicken – oder mit der Tastatur ansteuern und mit Enter öffnen.":
        "Καθημερινές λήψεις από τη φροντίδα του. Κάντε κλικ για μεγέθυνση – ή πλοηγηθείτε με το πληκτρολόγιο και ανοίξτε με Enter.",
    "Letzte Aktualisierung: 21. Juli 2026": "Τελευταία ενημέρωση: 21 Ιουλίου 2026",
    "Letzte Aktualisierung des Profils: 17. Juli 2026": "Τελευταία ενημέρωση προφίλ: 17 Ιουλίου 2026",
    "vor der Ausreise vorgesehen (FIV- und FeLV-Test).": "προβλέπεται πριν την αναχώρηση (τεστ FIV και FeLV).",
    "Ein FIV- und FeLV-Test wird vor der Ausreise durchgeführt.":
        "Πραγματοποιείται τεστ FIV και FeLV πριν την αναχώρηση.",
    "Andere Katzen möglich": "Άλλες γάτες πιθανές",
    "Gut mit anderen Katzen": "Καλά με άλλες γάτες",
    "Friedlich mit Artgenossen": "Ειρηνική με άλλες γάτες",
    "Verhalten mit Katzen": "Συμπεριφορά με γάτες",
    "geimpft": "εμβολιασμένη",
    "kastriert": "στειρωμένος",
    "sterilisiert": "στειρωμένη",
    "EKH-Mix": "ημίαιμη κοντότριχη",
    "Wohnungshaltung oder gesicherter Freigang": "Εσωτερικός χώρος ή ασφαλής εξωτερική πρόσβαση",
    "Ruhige Atmosphäre": "Ήρεμη ατμόσφαιρα",
    "Eigene Rückzugsorte": "Δικά της σημεία απόσυρσης",
    "Rückzugsorte": "Σημεία απόσυρσης",
    "Rückzug möglich": "Δυνατότητα απόσυρσης",
    "Details werden bei Ausreise ergänzt.": "Λεπτομέρειες θα προστεθούν κατά την αναχώρηση.",
    "ca. 2023": "περ. 2023",
    "Haltungsform nach Prüfung": "Τρόπος διαβίωσης μετά από έλεγχο",
    "Menschen, die bleiben": "Άνθρωποι που μένουν",
    "Ruhig und liebevoll": "Ήρεμα και στοργικά",
    "Andere Katzen? Individuell": "Άλλες γάτες; Κατά περίπτωση",
    "Wir machen bewusst keine Aussage über Befunde, die noch nicht vorliegen. Alle medizinischen Angaben geben den Stand wieder, der uns zum Zeitpunkt der letzten Aktualisierung bekannt war.":
        "Σκόπιμα δεν κάνουμε δηλώσεις για ευρήματα που δεν υπάρχουν ακόμη. Όλα τα ιατρικά στοιχεία αποτυπώνουν όσα γνωρίζαμε κατά την τελευταία ενημέρωση.",
}
