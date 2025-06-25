print("Zadejte čísla (končící nulou): ") # Text pri spusteni programu

# "startovaci" hodnota z ktere se pricita
soucet = 0
pocet = 0

# while na pricitani do cisel souctu a poctu + zadavani cisel
while True:
    cislo = int(input())

    if cislo == 0: # pokud se zada 0 tak se program "rozbije"
        break
    
    soucet += cislo
    pocet += 1 

if pocet > 0:
    prumer =  soucet / pocet # vypocet prumeru

    # Vypis "statistiky"
    print("Počet čísel: ", pocet)
    print("Součet čísel: ", soucet)
    print("Průměr čísel: ", prumer)
else:
    print("NEBYLA ZADÁNA ČÍSLA!") # err pokud nebyla zadana cisla