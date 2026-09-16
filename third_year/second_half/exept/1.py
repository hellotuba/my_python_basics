try:
 a = int(input("Zadej první číslo: "))
 b = int(input("Zadej druhé číslo: "))
 vysledek = a / b
 print("Výsledek je:", vysledek)
except ZeroDivisionError:
 print("Nelze dělit nulou!") 