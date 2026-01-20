<img width="1366" height="1024" alt="IMG_1588" src="https://github.com/user-attachments/assets/4df27317-3669-4dde-9bc1-80922ce83c6d" />
📊 Kaufmännische BK2 Tools
Digitalisierung kaufmännischer Prozesse mit Python
Dieses Repository enthält eine modulare Werkzeugsammlung, die speziell zur Automatisierung und Validierung kaufmännischer Berechnungen im Rahmen des Berufskollegs 2 (BK2) entwickelt wurde. Das Ziel des Projekts war es, komplexe theoretische Kalkulationsschemata in eine funktionale, benutzerfreundliche Software zu überführen.

🚀 Kernfunktionen
Das Toolkit umfasst vier Hauptmodule, die zentrale Bereiche der Betriebswirtschaftslehre abdecken:
• Lohn- & Gehaltsabrechnung (gehalt.py):
• Vollständige Berechnung vom Bruttogehalt bis zum Auszahlungsbetrag.
• Berücksichtigung aktueller Sozialversicherungswerte (BBG 2025/2026).
• Integration von Kirchensteuer, PV-Zuschlägen (nach Kinderanzahl) und vermögenswirksamen Leistungen (vL).
• Highlight: Automatische Generierung der korrekten Buchungssätze für die Finanzbuchhaltung.
• Quantitativer Angebotsvergleich (angebot.py):
• Vergleich mehrerer Lieferantenangebote auf Basis des Bezugspreises.
• Abbildung des vollständigen Einkaufskalkulationsschemas (Listeneinkaufspreis → Zieleinkaufspreis → Bareinkaufspreis → Bezugspreis).
• Deckungsbeitragsrechnung & KLR (stueck.py):
• Ermittlung des Stückdeckungsbeitrags (\bm{db}) und des Gesamtdeckungsbeitrags (\bm{DB}).
• Berechnung des Betriebsergebnisses, der kurzfristigen Preisuntergrenze (\bm{PUG}) und der Gewinnschwelle (Break-even-point).
• Wissenschaftlicher Taschenrechner (main_tr.py):
• Zusatzmodul für schnelle kaufmännische Nebenrechnungen inkl. Potenzen, Wurzeln und Logarithmen.

🛠 Technischer Stack & Konzepte
Bei der Umsetzung wurde besonderer Wert auf professionelle Software-Prinzipien gelegt:
• Modularisierung: Trennung von Programmlogik, Benutzerschnittstelle und Hilfsfunktionen zur besseren Wartbarkeit.
• Datensicherheit & Validierung: Implementierung eines robusten Error-Handlings (try-except Blöcke in tool.py), um Fehlermeldungen bei falschen Dateneingaben zu verhindern.
• User Experience: Dynamische Anpassung von Nachkommastellen und klare Benutzerführung in der Konsole.

📂 Struktur📂 Struktur
├── main.py          # Zentrales Hauptmenü und Programmsteuerung
├── tool.py          # Hilfswerkzeuge für Validierung und Formatierung
├── gehalt.py        # Modul Gehaltsrechnung
├── angebot.py       # Modul Angebotsvergleich
├── stueck.py        # Modul Deckungsbeitrag/KLR
├── rechnen.py       # Mathematische Logik für den Taschenrechner
└── main_tr.py       # Interface für den Taschenrechner
