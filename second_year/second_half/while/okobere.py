import random

body = 0

while True:
    print("Chceš hrát?(ano/ne) tvoje body:", body)
    pokracovat = input("Zadej: ")
    if pokracovat == "ne":
        print("CELKEVÉ BODY: ", body)
        break
    elif pokracovat == "ano":
        cislo = random.randint(2, 10)
        print("Tvoje karta: ", cislo)
        body += cislo
    if body == 21:
        print("CELKEVÉ BODY: ", body)
        print("VYHRÁL SI!")
        break
    elif body > 21:
        print("CELKEVÉ BODY: ", body)
        print("PROHRÁL SI!")
        break