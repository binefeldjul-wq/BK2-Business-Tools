import tool
def start_programm(frac):
    print(f"Willkommen zu Julian Binefelds Deckungsbeitragsrechnung. ")
    print("")
    
    #Hinweise
    print("Hinweis: Bei dezimalen Zahlen Punkt statt Komma benutzen. z. B. 2,9 Eingabe 2.9 ")
    print("Hinweis: Bei Prozenten nur die Zahl ohne %-Zeichen. z. B. 30% Eingabe 30. ")
    print("")
    anzahl_DB = tool.sicherung_int("Wie viele verschiedene Produkte gibt es? ")
    summe_DB = 0
    
    #Barverkaufspreis (p)
    for _ in range(anzahl_DB):
        question_1 = tool.sicherung_entsch("Ist p gegeben? j=ja/n=nein ")
        question_2 = tool.sicherung_entsch("Ist kv gegeben? j=ja/n=nein ")
        produkt = tool.sicherung_str("Produktbezeichnung ")
        
        if question_1 == "j":  #Barverkaufspreis ist gegeben
            p = tool.sicherung_float("Wie hoch ist p? ")
        
        #Barverkaufspreis wird berechnet
        else:
            listenverkaufspreis = tool.sicherung_float("Wie hoch ist der Listenverkaufspreis? ")  #Listenverkaufspreis
            rabatt = tool.sicherung_float("Wie viel % Rabatt gibt es? ")  #Rabatt
            skonto = tool.sicherung_float("Wie viel % Skonto gibt es? ")  #Skonto
            zielverkaufspreis = listenverkaufspreis * (1 - rabatt / 100)                 #Zielverkaufspreis
            p = zielverkaufspreis * (1 - skonto / 100)  #Barverkaufspreis
        
        #Variable Stückkosten (kv)
        if question_2 == "j": #Variable Stückkosten gegeben
            kv = tool.sicherung_float("Wie hoch ist kv? ")
        
        #Variable Stückkosten (kv) werden berechnet
        else:
            eigenkosten = tool.sicherung_float("Wie hoch sind die Eigenkosten? ") #Eigenkosten
            variable_gemeinkosten = tool.sicherung_float("Wie viel % variable Gemeinkosten gibt es? ")
            kv = eigenkosten * (1 + variable_gemeinkosten / 100)  #variable Stückkosten
        
        #Stückdeckungsbeitrag (db)
        db = p - kv 
        print("")
        tool.dynammische_dezimal("Der Stückdeckungsbeitrag", db, frac)
        print("")
        
        #Deckungsbeitrag (DB)
        menge = tool.sicherung_int("Wie viel Menge wird produziert? ")  #Produktionsmenge
        DB = db * menge
        print("")
        tool.dynammische_dezimal("Der Deckungsbeitrag", DB, frac)
        print("")
        summe_DB += DB
        
        #Kurzfristige Preisuntergrenze (PUG)
        kurzfristige_pug = kv
        
    #Betriebsergebnis (BE)
    fixkosten_gesamt = tool.sicherung_float("Wie hoch sind die gesamten Fixkosten? ") #Fixkosten
    BE = summe_DB - fixkosten_gesamt  #Betriebsergebnis
    
    #Gewinn / Verlust
    if BE > 0:
        tool.dynammische_dezimal("Das Betriebsergebnis", BE, frac)
    else:
        tool.dynammische_dezimal("Das Betriebsergebnis", BE, frac)
    tool.dynammische_dezimal("Die Kurzfristige Preisuntergrenze", kurzfristige_pug, frac)
    
    #Break-even-point
    break_even_point = fixkosten_gesamt / db 
    print(f"Menge bei der Gewinn = 0 ist ab einer Menge von {break_even_point:,.{frac}f}. ")
    print("Programm beendet.")