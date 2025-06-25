print("Zadejte řadu čísel (končící nulou): ") # Text pri spusteni programu

# "startovaci" hodnota z ktere se pricita
cisla = []
pocet_sudy = 0
pocet_lichy = 0

# while na pricitani do cisel lich. a sude + zadavani cisel
while True:
    cislo = int(input())

    if cislo == 0: # pokud se zada 0 tak se program "rozbije"
        break

    cisla.append(cislo)

    if cislo % 2 == 0:  # pripocet pokud je cislo sude
        pocet_sudy += 1
    else: # pokud je liche
        pocet_lichy += 1

if cisla: 
    nejmensi = min(cisla) # nejmensi cislo (funkce min)
    nejvetsi = max(cisla) # nejvetsi cislo (funkce max)

    # Vypis "statistiky"
    print("Nejmenší číslo: ", nejmensi)
    print("Nejvetší číslo: ", nejvetsi)
    print("Počet lichých čísel: ", pocet_lichy)
    print("Počet sudých čísel: ", pocet_sudy)
else:
    print("NEBYLA ZADÁNA ČÍSLA!") # err pokud nebyla zadana cisla