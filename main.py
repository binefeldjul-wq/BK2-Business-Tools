#Importieren der drei Pythonskripte
import angebot
import gehalt
import stueck
import tool

def menu():
    dezimal = 2
    while True:
        print(f"\n" + "="*30)
        print(f"Willkommen zu Julian Binefelds KAUFMÄNNISCHES BK2 TOOLS. ")
        print(f"="*30)
        print(f"1. Gehaltsrechner")
        print(f"2. Angebotsvergleich")
        print(f"3. Deckungsbeitrag")
        print(f"4. Einstellungen")
        print(f"5. Beenden")
        
        wahl = input("Was möchtest du tun? (1-4): ")
        if wahl == "1":
            gehalt.start_programm(dezimal)
        
        elif wahl == "2":
            angebot.start_programm(dezimal)
            
        elif wahl == "3":
            stueck.start_programm(dezimal)
        
        elif wahl == "4":
            dezimal = tool.dezimal_ändern()
            
        elif wahl == "5":
            print(f"Programm geschlossen. ")
            break
        else:
            print(f"Fehler: Bitte wähle 1, 2, 3, 4 oder 5. ")
if __name__ == "__main__":
    menu()