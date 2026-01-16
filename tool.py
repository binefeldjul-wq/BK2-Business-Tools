#Dezimalstellen ändern
def dezimal_ändern():
    dezimal_ändern = sicherung_entsch("Möchtest du mit 2 Nachkommastellen rechnen oder ändern? j = ja/ n = nein")
    if dezimal_ändern == "j":
        dezimal = sicherung_int("Dezimal Kommastellen")
    else:
        dezimal = 2
    return dezimal

#Dynammische Dezimalnachkommastellen
def dynammische_dezimal(beschreibung, wert, frac):
    print(f"{beschreibung} beträgt: {wert:,.{frac}f} €")
    
#Sicherung für Ganzzahlen
def sicherung_int(aufforderung):
    while True:
        try:
            eingabe = int(input(aufforderung))
            return eingabe
        except ValueError:
            print("Fehler: Bitte eine ganze Zahl eingeben! z. B. 100 ")

#Sicherung für Kommazahlen
def sicherung_float(aufforderung):
    while True:
        try:
            eingabe = float(input(aufforderung))
            return eingabe
        except ValueError:
            print("Fehler: Bitte eine Zahl eingeben! z. B. 2.98 ")

#Sicherung für Text
def sicherung_str(aufforderung):
    while True:
        try:
            eingabe = input(aufforderung).title().strip() #title Anfangsgroßschreibung
            return eingabe
        except ValueError:
            print("Fehler: Bitte Text eingeben! ")

#Sicherung für Ja/ Nein
def sicherung_entsch(aufforderung):
    while True:
        try:
            eingabe = input(aufforderung).lower().strip() #lower Anfangskleinschreibung
            if eingabe in ["j", "n"]:
                return eingabe
            else:
                print("Fehler: Bitte j oder n eingeben! ")
            
    