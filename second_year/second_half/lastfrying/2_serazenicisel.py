# Napište program, který umožní: 1. Zadávat čísla uživatelem 2. Seřadit čísla vzestupně nebo sestupně Zadání: 1. Umožněte uživateli zadávat čísla, dokud nezadá nulu. 2. Po zadání všech čísel se uživatele zeptejte, zda chce čísla seřadit vzestupně nebo sestupně. 3. Seřaďte čísla podle volby uživatele a vypište je.

def seradit_cisla(cisla, smer):
    if smer == '1':
        return sorted(cisla)
    elif smer == '2':
        return sorted(cisla, reverse=True)
    else:
        print("Neplatný směr řazení. Používám výchozí vzestupné řazení.")
        return sorted(cisla)

def main():
    cisla = []
    while True:
        try:
            vstup = int(input("Zadejte číslo (pro ukončení zadejte 0): "))
            if vstup == 0:
                break
            cisla.append(vstup)
        except ValueError:
            print("Zadejte platné celé číslo.")
    if not cisla:
        print("Seznam čísel je prázdný.")
    if cisla:
        smer = input("Chcete čísla seřadit vzestupně nebo sestupně? (zadejte '1' nebo '2'): ")
        serazena_cisla = seradit_cisla(cisla, smer)
        print("Seřazená čísla:", serazena_cisla)
    else:
        print("Žádná čísla nebyla zadána.")

if __name__ == "__main__":
    main()