import tool
import math as m

#Addition
def addition():
    print("")
    summand_1 = tool.sicherung_float("Eine Zahl eingeben! ")
    summand_2 = tool.sicherung_float("Eine zweite Zahl eingeben! ")
    print("")
    summe = summand_1 + summand_2
    return summe
        
#Subtraktion
def subtraktion():
    print("")
    minuend = tool.sicherung_float("Eine Zahl eingeben! ")
    subtrahend = tool.sicherung_float("Eine Zeite Zahl eingeben! ")
    print("")
    differenz = minuend - subtrahend
    return differenz
            
#Multiplikation
def multiplikation():
    print("")
    faktor_1 = tool.sicherung_float("Erste Zahl eingeben! ")
    faktor_2 = tool.sicherung_float("Eine zweite Zahl eingeben! ")
    print("")
    produkt = faktor_1 * faktor_2
    return produkt
            
#Division
def division():
    print("")
    divident = tool.sicherung_float("Eine Zahl eingeben! ")
    divisor = tool.sicherung_float("Eine zweite Zahl eingeben! ")
    print("")
    quotient = divident / divisor
    return quotient

#Potenzion
def potenzion():
    print("")
    basis = tool.sicherung_float("Eine basis eingeben! ")
    exponent = tool.sicherung_float("Einen Exponenten eingeben! ")
    print("")
    potenz_ergebnis = basis ** exponent
    return potenz_ergebnis

#Wurzelziehen
def wurzelziehen():
    print("")
    wurzel = tool.sicherung_float("Welche Wurzel? ")
    radikant = tool.sicherung_float("Was steht unter der Wurzel? ")
    print("")
    wurzelergebnis = radikant ** (1 / wurzel)
    return wurzelergebnis

#Logarithmieren
def logarithmieren():
    print("")
    basis = tool.sicherung_float("Logarithmus zu welcher Basis? ")
    zahl_log = tool.sicherung_float("Was steht im Logarithmus? ")
    print("")
    log_ergebnis = m.log(zahl_log) / m.log(basis) #log(y) = Basis
    return log_ergebnis