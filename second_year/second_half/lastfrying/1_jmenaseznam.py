# Napište program, který umožní: vyhledat jméno v seznamu přidat nové jméno do seznamu odebrat jméno ze seznamu vypsat celý seznam seřazený abecedně

jmena = []
def vyhledat_jmeno(jmeno):
    if jmeno in jmena:
        print(f"Jméno '{jmena}' bylo nalezeno.")
    else:
        print(f"Jméno '{jmeno}' nebylo nalezeno.")

def pridat_jmeno(jmeno):
    if jmeno not in jmena:
        jmena.append(jmeno)
        print(f"Jméno '{jmeno}' bylo přidáno.")
    else:
        print(f"Jméno '{jmeno}' již v seznamu existuje.")

def odebrat_jmeno(jmeno):
    if jmeno in jmena:
        jmena.remove(jmeno)
        print(f"Jméno '{jmeno}' bylo odebráno.")
    else:
        print(f"Jméno '{jmeno}' nebylo nalezeno v seznamu.")

def vypis_seznam():
    if jmena:
        print("Seznam jmen (Podle abededy):")
        for jmeno in sorted(jmena):
            print(jmeno)
    else:
        print("Seznam jmen je prázdný.")

def main():
    while True:
        print("\n1. Vyhledat jméno")
        print("2. Přidat nové jméno")
        print("3. Odebrat jméno")
        print("4. Vypsat celý seznam")
        print("5. Konec")
        volba = int(input("Zadejte číslo volby: "))

        if volba == 1:
            jmeno = input("Zadejte jméno k vyhledání: ")
            print(" ")
            vyhledat_jmeno(jmeno)
        elif volba == 2:
            jmeno = input("Zadejte jméno k přidání do seznamu: ")
            print(" ")
            pridat_jmeno(jmeno)
        elif volba == 3:
            jmeno = input("Zadejte jméno k odebrání ze seznamu: ")
            print(" ")
            odebrat_jmeno(jmeno)
        elif volba == 4:
            print(" ")
            vypis_seznam()
        elif volba == 5:
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()
