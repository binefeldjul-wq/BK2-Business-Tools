import tool
def start_programm(frac):
    print("Willkommen zu Julian Binefelds quantitativen Angebotsvergleich.")
    print("")
    
    #Hinweise
    print("Hinweis: Bei dezimalen Zahlen Punkt statt Komma benutzen. z. B. 2,9 Eingabe 2.9")
    print("Hinweis: Bei Prozenten nur die Zahl ohne %-Zeichen. z. B. 30% Eingabe 30. ")
    
    print("")
    anzahl = 0 
    anzahl_angebote = sicherung_int("Wie viele Angebote haben wir bekommen? ")
    for _ in range (anzahl_angebote):
        #Eingaben 
        lieferranten = sicherung_str("Welcher Lieferrant bietet uns das Produkt an? ")
        menge = sicherung_float("Wie viel Menge wird eingekauft? ")
        listeneinkaufspreis_menge = sicherung_float("Wie hoch ist der Listeneinkaufspreis pro Menge? ")
        lieferrabatt = sicherung_float("Wie viel % Lieferrabatt gibt es? ")
        lieferskonto = sicherung_float("Wie viel % Lieferskonto gibt es? ")
        bezugskosten = sicherung_float("Wie viel Euro Bezugskosten gibt es? ")
        print("")
        #Verarbeitung
        listeneinkaufspreis = listeneinkaufspreis_menge * menge
        
        lieferrabatt_euro = listeneinkaufspreis * lieferrabatt / 100
        zieleinkaufspreis = listeneinkaufspreis - lieferrabatt_euro
        
        lieferskonto_euro = zieleinkaufspreis * lieferskonto / 100
        bareinkaufspreis = zieleinkaufspreis - lieferskonto_euro
        
        bezugspreis = bareinkaufspreis + bezugskosten
        bezugspreis_menge = bezugspreis / menge
        
        anzahl += 1
        
        #Ausgabe
        print(f" {anzahl} {lieferranten}. ")
        print("")
        dynammische_dezimal("Der Listeneinkaufspreis", listeneinkaufspreis, frac)
        dynammische_dezimal("Der Lieferrabatt", lieferrabatt_euro, frac)
        dynammische_dezimal("Der Zieleinkaufspreis", zieleinkaufspreis, frac)
        dynammische_dezimal("Der Lieferskonto", lieferskonto_euro, frac)
        dynammische_dezimal("Der Bareinkaufspreis", bareinkaufspreis, frac)
        dynammische_dezimal("Die Bezugskosten", bezugskosten, frac)
        dynammische_dezimal("Der Bezugspreis", bezugspreis, frac)
        dynammische_dezimal("Der Bezugspreis pro Menge", bezugspreis_menge, frac)
        print("")
    print("Programm beendet. ")
    
    
if __name__ == "__main__":
    start_programm()