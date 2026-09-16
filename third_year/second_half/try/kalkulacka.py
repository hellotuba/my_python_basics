try:
    a = float(input("Zadej první číslo: "))
    b = float(input("Zadej druhé číslo: "))
    vysledek = a / b
    print("Výsledek:", vysledek)
except ValueError:
    print("Chyba: Zadal jsi nečíselný vstup!")
except ZeroDivisionError:
    print("Chyba: Nelze dělit nulou!")