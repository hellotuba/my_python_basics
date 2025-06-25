# Vytvořte program, který ze seznamu vybere, každé n-té číslo. A zobrazí seznam.
import random

seznam = [random.randint(1, 100) for _ in range(50)]
print("Seznam čísel:", *seznam)
n = int(input("Zadejte hodnotu n: "))
if n <= 0:
    print("Hodnota n musí být kladná.")
else:
    vybrana_cisla = seznam[n-1::n]
    print(f"Každé {n}-té číslo ze seznamu je:", *vybrana_cisla)

