# zada cislo zdali je kladne ci zaporne nebo rovno 0
a = int(input("Zadej číslo: "))

if a == 0:
    print("Nulové číslo")
elif a > 0:
    print("Pozitivní")
elif a < 0:
    print("Negativní")