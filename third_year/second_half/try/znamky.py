try:
    znamka1 = float(input("Zadej první známku: "))
    znamka2 = float(input("Zadej druhou známku: "))
    prumer = (znamka1 + znamka2) / 2
    print(f"Průměrná známka: {prumer}")
except ValueError:
    print("Chyba: Zadej platná čísla!")