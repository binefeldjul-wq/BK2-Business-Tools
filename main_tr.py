import rechnen
import tool

def start_programm(frac):
    def menu():
        while True:
            print(f"="*70)
            print("Willkommen zum Taschenrechner. ")
            print(f"="*70)
            print("")
            print("1. Addition ")
            print("2. Subtraktion ")
            print("3. Multiplikation ")
            print("4. Division ")
            print("5. Potenzion. ")
            print("6. Wurzelziehen. ")
            print("7. Logarithmieren. ")
            print("8. Programm beenden. ")
            print(f"="*70)
            print("")
            
            #Variablen
            wahl = tool.sicherung_str("Was möchtest du tun? Wähle zwischen (1-8). ")
            
            if wahl == "1":
                neu_addition = rechnen.addition()
                print(f"{neu_addition:,.{frac}f}")
                print("")
            
            elif wahl == "2":
                neu_subtraktion = rechnen.subtraktion()
                print(f"{neu_subtraktion:,.{frac}f}")
                print("")
                
            elif wahl == "3":
                neu_multiplikation = rechnen.multiplikation()
                print(f"{neu_multiplikation:,.{frac}f}")
                print("")
                        
            elif wahl == "4":
                neu_division = rechnen.division()
                print(f"{neu_division:,.{frac}f}")
                print("")
                
            elif wahl == "5":
                neu_potenzion = rechnen.potenzion()
                print(f"{neu_potenzion:,.{frac}f}")
                print("")
            
            elif wahl == "6":
                neu_wurzel = rechnen.wurzelziehen()
                print(f"{neu_wurzel:,.{frac}f}")
                print("")
                
            elif wahl == "7":
                neu_log = rechnen.logarithmieren()
                print(f"{neu_log:,.{frac}f}")
                print("")
                
            elif wahl == "8":
                print("Programm beenden. ")
                break
            else:
                print("")
                print("Fehler: Bitte wähle zwischen (1-8) ")
                print("")
    menu()