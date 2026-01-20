import tool
def start_programm(frac):
    print("Willkommen zu Julian Binefelds Gehaltsrechner. ")
    print("")
    
    #Hinweise
    print("Hinweis: Bei dezimalen Zahlen Punkt statt Komma benutzen. z. B. 2,9 Eingabe 2.9 ")
    print("Hinweis: Bei Prozenten nur die Zahl ohne %-Zeichen. z. B. 30% Eingabe 30. ")
    
    print("")
    mitarbeiter = tool.sicherung_str("Wie heißt der Mitarbeiter? ")
    bruttogehalt = tool.sicherung_float("Wie hoch ist dein Gehalt? ")
    vL_AG = tool.sicherung_float("Wie hoch ist vermögenswirksame Leistungen des AG? ")
    vS = tool.sicherung_float("Wie hoch ist das vermögenswirksame Sparen? ")
    question_1 = tool.sicherung_entsch("Ist die Lohnsteuer gegeben? j=ja/n=nein ")
    KiSt = tool.sicherung_float("Wie viel % Kirchensteuer gibt es? ")
    question_3 = tool.sicherung_int("Von Welchem Jahr möchtst du die BBG wählen 2025/2026? ")
    Zusatzbeitrag = tool.sicherung_float("Wie hoch ist der Zusatzbeitrag? ")
    question_2 = tool.sicherung_int("Wie viele Kinder gibt es? ")
    vorschuss = tool.sicherung_float("Wie viel Vorschuss gibt es? ")
    print("")
    
    #Beitragsbemessungsgrenzen 2025
    Beitragsbemessungsgrenze_RV_AV_2025 = 8050.00
    Beitragsbemessungsgrenze_KV_PV_2025 = 5512.50
    
    #Beitragsbemessungsgrenzen 2026
    Beitragsbemessungsgrenze_RV_AV_2026 = 8450.00
    Beitragsbemessungsgrenze_KV_PV_2026 = 5812.50
    
    if question_3 == 2025:
        Beitragsbemessungsgrenze_RV_AV = Beitragsbemessungsgrenze_RV_AV_2025
        Beitragsbemessungsgrenze_KV_PV = Beitragsbemessungsgrenze_KV_PV_2025
    elif question_3 == 2026:
        Beitragsbemessungsgrenze_RV_AV = Beitragsbemessungsgrenze_RV_AV_2026
        Beitragsbemessungsgrenze_KV_PV = Beitragsbemessungsgrenze_KV_PV_2026
    else:
        print("Fehler: Bitte 2025/ 2026 wählen! ")
    print("")
    
    st_sv_gehalt = bruttogehalt + vL_AG
    
    if question_1 == "j":
        lohnsteuer = tool.sicherung_float("Wie hoch ist die Lohnsteuer? ")
        KiSt_euro = lohnsteuer * KiSt / 100
    else:
        lohnsteuer = tool.sicherung_float("Die Lohnsteuer aus Lohnsteuertabelle rauslesen. ")
        KiSt_euro = tool.sicherung_float("KiSt aus Lohnsteuertabelle rauslesen. ")
    
    steuern = lohnsteuer + KiSt_euro
    print("")
    
    #Beitragssätze der Sozialversicherungen
    RV_Beitragssatz = 18.6
    AV_Beitragssatz = 2.6
    KV_Beitragssatz = 14.6
    
    #Berechnung des Arbeitnehmer/Arbeitgeberanteils (50/50)
    RV_AN_anteil = RV_Beitragssatz / 200
    AV_AN_anteil = AV_Beitragssatz / 200
    KV_AN_anteil = (KV_Beitragssatz + Zusatzbeitrag) / 200
    
    if  question_2 >= 1 and question_2 < 5:
        PV_Beitragssatz_AN = 1.8 - 0.25 * (question_2 - 1)
    elif question_2 >= 5:
        PV_Beitragssatz_AN = 0.8
    else:
        PV_Beitragssatz_AN = 2.4
    PV_AN_anteil = PV_Beitragssatz_AN / 100
    
    PV_Beitragssatz_AG = 1.8
    PV_AG_anteil = PV_Beitragssatz_AG / 100
    print("")
    
    #Berechnung RV/AV
    if st_sv_gehalt >= Beitragsbemessungsgrenze_RV_AV:
        RV = Beitragsbemessungsgrenze_RV_AV * RV_AN_anteil
        AV = Beitragsbemessungsgrenze_RV_AV * AV_AN_anteil
    else:
        RV = st_sv_gehalt * RV_AN_anteil
        AV = st_sv_gehalt * AV_AN_anteil
    
    #Berechnung KV/PV
    if st_sv_gehalt >= Beitragsbemessungsgrenze_KV_PV:
        KV = Beitragsbemessungsgrenze_KV_PV * KV_AN_anteil
        PV_AN = Beitragsbemessungsgrenze_KV_PV * PV_AN_anteil
        PV_AG = Beitragsbemessungsgrenze_KV_PV * PV_AG_anteil
    else:
        KV = st_sv_gehalt * KV_AN_anteil
        PV_AN = st_sv_gehalt * PV_AN_anteil
        PV_AG = st_sv_gehalt * PV_AG_anteil
    
    sv_AN_anteil = RV + AV + KV + PV_AN
    sv_AG_anteil = RV + AV + KV + PV_AG
    sv_anteil = sv_AN_anteil + sv_AG_anteil
    nettogehalt = st_sv_gehalt - steuern - sv_AN_anteil
    
    überweisungbetrag = nettogehalt - vS - vorschuss
    print("")
    #Ausgaben
    print(mitarbeiter )
    tool.dynammische_dezimal("Das Bruttogehalt", bruttogehalt, frac)
    tool.dynammische_dezimal("Der AG-Anteil der vermögenswirksamen Leistungen", vL_AG, frac)
    tool.dynammische_dezimal("Das Steuern und Sozialversicherungspflichtige Gehalt", st_sv_gehalt, frac)
    print("")
    tool.dynammische_dezimal("Die Lohnsteuer", lohnsteuer, frac)
    tool.dynammische_dezimal("Die Kirchensteuer", KiSt_euro, frac)
    print("")
    tool.dynammische_dezimal("KV", KV, frac)
    tool.dynammische_dezimal("RV", RV, frac)
    tool.dynammische_dezimal("AV", AV, frac)
    tool.dynammische_dezimal("PV-AN", PV_AN, frac)
    print("")
    tool.dynammische_dezimal("Das Nettogehalt", nettogehalt, frac)
    tool.dynammische_dezimal("Das vermögenswirksame Sparen", vS, frac)
    tool.dynammische_dezimal("Der Vorschuss", vorschuss, frac)
    print("")
    tool.dynammische_dezimal("Der Überweisungsbetrag", überweisungbetrag, frac)
    
    #Buchungssätze
    print(f"1. Buchung der Abführung der Sozialversicherungsbeitraäge. ")
    print("")
    print(f"2640 SV-Vorrauszahlung {sv_anteil:,.{frac}f} € ")
    print(f"   an 2800 Bank {sv_anteil:,.{frac}f} € ")
    print("")
    print(f"2. Buchung des Gehalts. ")
    print("")
    print(f"6300 Gehälter {st_sv_gehalt:,.{frac}f} € ")
    print(f"   an 2800 Bank {überweisungbetrag:,.{frac}f} € ")
    print(f"   an 4830 sonstige Verb gegenüber FB {steuern:,.{frac}f} € ")
    print(f"   an 2640 SV-Vorrauszahlung {sv_AN_anteil:,.{frac}f} € ")
    print(f"   an 2650 Vorschüsse {vorschuss:,.{frac}f} € ")
    print(f"   an 4860 Verb aus vL {vS:,.{frac}f} € ")
    print("")
    print(f"3. Buchung des Arbeitgeberanteils zur Sozialversicherung. ")
    print("")
    print(f"6400 Arbeitgeberanteil zur SV {sv_AG_anteil:,.{frac}f} € ")
    print(f"   an 2640 SV-Vorrauszahlung {sv_AG_anteil:,.{frac}f} € ")
    print("")
    print(f"4. Buchung der Abführung der Lohn- und Kirchensteuer. ")
    print("")
    print(f"4830 sonstige Verb gegenüber FB {steuern:,.{frac}f} € ")
    print(f"4860 Verb aus vL {vS:,.{frac}f} € ")
    print(f"   an 2800 Bank {(steuern + vS):,.{frac}f} € ")
    print("")
    print("Programm beendet. ")