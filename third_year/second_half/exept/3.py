seznam = ["jablko", "banán", "třešeň", "hruška"]

try:
    index = int(input("Zadej index: "))
    print(seznam[index])
except IndexError:
    print("Index je mimo rozsah seznamu!")
except ValueError:
    print("Zadej prosím celé číslo!")