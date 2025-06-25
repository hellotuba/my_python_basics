#2. Napište program, který pro zadaný seznam finančních částek vypočítá celkovou daň. Bohatí (200 a víc peněz) platí daň 20 Kč. Ti, co nejsou bohatí, ale mají alespoň 100 peněz, platí daň 10 Kč. Ostatní daň neplatí.

import random

dan_list = [random.randint(10, 1000) for _ in range(50)] #dan_list = [0, 5, 0, 2, 4, 9] -- TEST PARAMETERS FOR if celkova_dan == 0 (error / no money)
print("Původní seznam částek:\n",dan_list)
celkova_dan = 0
for castka in dan_list:
    if castka >= 200:
        celkova_dan += 20
    elif castka >= 100:
        celkova_dan += 10
    else:
        celkova_dan += 0
if celkova_dan == 0: # HANDLER FOR ERROR THAT MAY NOT HAPPEN BUT STILL...
    print(" \n \n==========================================================")
    print("ERROR | ŽÁDNÁ ČASTKA PROGRAM NEVYGENEROVAL DOSTATEK PENĚZ")
else:
    print(" \n \n=============================")
    print("Celková daň z částek je:", celkova_dan)