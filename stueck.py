import tool
def start_programm(frac):
    print(f"Willkommen zu Julian Binefelds Deckungsbeitragsrechnung. ")
    print("")
    
    #Hinweise
    print("Hinweis: Bei dezimalen Zahlen Punkt statt Komma benutzen. z. B. 2,9 Eingabe 2.9 ")
    print("Hinweis: Bei Prozenten nur die Zahl ohne %-Zeichen. z. B. 30% Eingabe 30. ")
    print("")
    anzahl_DB = sicherung_int("Wie viele verschiedene Produkte gibt es? ")
    summe_DB = 0
    
    #Barverkaufspreis (p)
    for _ in range(anzahl_DB):
        question_1 = sicherung_entsch("Ist p gegeben? j=ja/n=nein ")
        question_2 = sicherung_entsch("Ist kv gegeben? j=ja/n=nein ")
        produkt = sicherung_str("Produktbezeichnung")
        
        if question_1 == "j":  #Barverkaufspreis ist gegeben
            p = sicherung_float("Wie hoch ist p? ")
        
        #Barverkaufspreis wird berechnet
        else:
            listenverkaufspreis = sicherung_float("Wie hoch ist der Listenverkaufspreis? ")  #Listenverkaufspreis
            rabatt = sicherung_float("Wie viel % Rabatt gibt es? ")  #Rabatt
            skonto = sicherung_float("Wie viel % Skonto gibt es? ")  #Skonto
            zielverkaufspreis = listenverkaufspreis * (1 - rabatt / 100)                 #Zielverkaufspreis
            p = zielverkaufspreis * (1 - skonto / 100)  #Barverkaufspreis
        
        #Variable Stückkosten (kv)
        if question_2 == "j": #Variable Stückkosten gegeben
            kv = sicherung_float("Wie hoch ist kv? ")
        
        #Variable Stückkosten (kv) werden berechnet
        else:
            eigenkosten = sicherung_float("Wie hoch sind die Eigenkosten? ") #Eigenkosten
            variable_gemeinkosten = sicherung_float("Wie viel % variable Gemeinkosten gibt es? ")
            kv = eigenkosten * (1 + variable_gemeinkosten / 100)  #variable Stückkosten
        
        #Stückdeckungsbeitrag (db)
        db = p - kv 
        print("")
        dynammische_dezimal("Der Stückdeckungsbeitrag", db, frac)
        print("")
        
        #Deckungsbeitrag (DB)
        menge = sicherung_int("Wie viel Menge wird produziert? ")  #Produktionsmenge
        DB = db * menge
        print("")
        dynammische_dezimal("Der Deckungsbeitrag", DB, frac)
        print("")
        summe_DB += DB
        
        #Kurzfristige Preisuntergrenze (PUG)
        kurzfristige_pug = kv
        
    #Betriebsergebnis (BE)
    fixkosten_gesamt = sicherung_float("Wie hoch sind die gesamten Fixkosten? ") #Fixkosten
    BE = summe_DB - fixkosten_gesamt  #Betriebsergebnis
    
    #Gewinn / Verlust
    if BE > 0:
        dynammische_dezimal("Das Betriebsergebnis", BE, frac)
    else:
        dynammische_dezimal("Das Betriebsergebnis", BE, frac)
    dynammische_dezimal("Die Kurzfristige Preisuntergrenze", kurzfristige_pug, frac)
    
    #Break-even-point
    break_even_point = fixkosten_gesamt / db 
    print(f"Menge bei der Gewinn = 0 ist ab einer Menge von {break_even_point:,.{frac}f}. ")
    print("Programm beendet.")
    
    
if __name__ == "__main__":
    start_programm()