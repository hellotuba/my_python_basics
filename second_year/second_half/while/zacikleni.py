#zacikleni ciklu while
from random import randrange

cislo = randrange(100)

while True:
    print("číslo je:", cislo)
    print("Počkej až se počítč unaví...")
    
while True:
    opoved = input("Řekni ááá ")
    if opoved =="ááá":
        print("béé")
        break   # "rozbiti" neboli ukonceni ciklu
    print("Špatně")

print("HOTOVO!")