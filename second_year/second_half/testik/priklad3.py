print("Zadejte celkové částky z učetenek (končící nulou): ") # Text pri spusteni programu

# "startovaci" hodnota z ktere se pricita
celkovy_soucet = 0
drazsi = 0

# while na pricitani do castek a celkoveho + zadavani cisel
while True:

    castka = float(input())

    if castka == 0: # pokud se zada 0 tak se program "rozbije"
        break
    
    celkovy_soucet += castka

    if castka > 100: # pokud je castka vice nez 100 tak se pricte do drazsi
        drazsi += 1

print("Celková utracená částka", celkovy_soucet)
print("Nákupy dražší než 100: ", drazsi)