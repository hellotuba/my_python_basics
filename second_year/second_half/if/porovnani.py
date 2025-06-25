# porovnani 2 cisel cisla ziskate od uzivatele
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))

if a == b:
    print("Obě čísla se rovnají", a, "=", b)
elif a > b:
    print("První číslo je větší:", a)
elif a < b:
    print("Druhé číslo je větší:", b)