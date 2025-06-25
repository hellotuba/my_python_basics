import random

rcislo = random.randint(1, 10)
print("Uhádni číslo od 1 do 10")
pokus = 0

while True:
    gues = int(input())

    if gues > rcislo:
        print("Číslo je menší")
    elif gues < rcislo:
        print("Číslo je větší")
    elif gues == rcislo:
        print("Číslo bylo:", rcislo)
        break

    pokus += 1

print("KONEC! Pokusů:", pokus)