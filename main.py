#Importieren der drei Pythonskripte
import angebot
import gehalt
import stueck
import tool
import main_tr

def menu():
    dezimal = 2
    while True:
        print(f":"*70)
        print(f"Willkommen zu Julian Binefelds KAUFMÄNNISCHES BK2 TOOLS. ")
        print(f":"*70)
        
        print(f"1. Gehaltsrechner")
        print(f"2. Angebotsvergleich")
        print(f"3. Deckungsbeitrag")
        print(f"4. Taschenrechner")
        print(f"5. Nachkommastellen ändern z. B von 2 zu 3")
        print(f"6. Beenden")
        print(f":"*70)
        print("")
        
        wahl = input("Was möchtest du tun? (1-6): ")
        print("")
        if wahl == "1":
            gehalt.start_programm(dezimal)
        
        elif wahl == "2":
            angebot.start_programm(dezimal)
            
        elif wahl == "3":
            stueck.start_programm(dezimal)
        
        elif wahl == "4":
            main_tr.start_programm(dezimal)
        
        elif wahl == "5":
            dezimal = tool.dezimal_aendern(dezimal)
            
        elif wahl == "6":
            print(f"Programm geschlossen. ")
            break
        else:
            print(f"Fehler: Bitte wähle (1-6). ")
            print("")
menu()