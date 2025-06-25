zacatek = input("Zadejte slovo: ")
pismeno = int(input("Zadej pozici (od 0): "))
znak = input("Zadej znak: ")

# Replace "Hello" with "Hi"  
konec = zacatek[:pismeno] + znak + zacatek[pismeno + 1:]
print(konec)