try:
 cislo = int(input("Zadej číslo: "))
 print("Zadal/a jsi:", cislo)
except ValueError:
 print("Chyba: nezadal/a jsi číslo!")