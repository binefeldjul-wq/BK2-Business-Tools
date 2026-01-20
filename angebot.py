import tool
def start_programm(frac):
    print("Willkommen zu Julian Binefelds quantitativen Angebotsvergleich.")
    print("")
    
    #Hinweise
    print("Hinweis: Bei dezimalen Zahlen Punkt statt Komma benutzen. z. B. 2,9 Eingabe 2.9")
    print("Hinweis: Bei Prozenten nur die Zahl ohne %-Zeichen. z. B. 30% Eingabe 30. ")
    
    print("")
    anzahl = 0 
    anzahl_angebote = tool.sicherung_int("Wie viele Angebote haben wir bekommen? ")
    for _ in range (anzahl_angebote):
        #Eingaben 
        lieferranten = tool.sicherung_str("Welcher Lieferrant bietet uns das Produkt an? ")
        menge = tool.sicherung_float("Wie viel Menge wird eingekauft? ")
        listeneinkaufspreis_menge = tool.sicherung_float("Wie hoch ist der Listeneinkaufspreis pro Menge? ")
        lieferrabatt = tool.sicherung_float("Wie viel % Lieferrabatt gibt es? ")
        lieferskonto = tool.sicherung_float("Wie viel % Lieferskonto gibt es? ")
        bezugskosten = tool.sicherung_float("Wie viel Euro Bezugskosten gibt es? ")
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
        tool.dynammische_dezimal("Der Listeneinkaufspreis", listeneinkaufspreis, frac)
        tool.dynammische_dezimal("Der Lieferrabatt", lieferrabatt_euro, frac)
        tool.dynammische_dezimal("Der Zieleinkaufspreis", zieleinkaufspreis, frac)
        tool.dynammische_dezimal("Der Lieferskonto", lieferskonto_euro, frac)
        tool.dynammische_dezimal("Der Bareinkaufspreis", bareinkaufspreis, frac)
        tool.dynammische_dezimal("Die Bezugskosten", bezugskosten, frac)
        tool.dynammische_dezimal("Der Bezugspreis", bezugspreis, frac)
        tool.dynammische_dezimal("Der Bezugspreis pro Menge", bezugspreis_menge, frac)
        print("")
    print("Programm beendet. ")