cislo = int(input("Zadej cislo (0-99999): "))

jednotkove = ["nula", "jedna", "dva", "tri", "ctyri", "pet", "sest", "sedm", "osm", "devet"]
desetvicedodvaceti = ["deset", "jedenact", "dvanact", "trinact", "ctyrnact", "patnact", "sestnact", "sedmnact", "osmnact", "devatenact"]
desitkove = ["", "deset", "dvacet", "tridcet", "ctyricet", "padesat", "sedesat", "sedmdesat", "osmdesat", "devadesat"]
stovkove = ["", "sto", "dvesta", "trista", "ctyri sta", "pet set", "sest set", "sedm set", "osm set", "devet set"]
tisicovkove = ["", "tisic", "dva tisice", "tri tisice", "ctyri tisice", "pet tisic", "sest tisic", "sedm tisic", "osm tisic", "devet tisic"]
desetitisicovkove = ["", "deset tisic", "dvacet tisic", "tridcet tisic", "ctyricet tisic", "padesat tisic", "sedesat tisic", "sedmdesat tisic", "osmdesat tisic", "devadesat tisic"]

if cislo < 0 or cislo > 99999:
    print("Číslo je mimo rozsah programu. (0-99999)")
else:
    desetitisice = (cislo // 10000)
    tisice = (cislo % 10000) // 1000
    stovky = (cislo % 1000) // 100
    desitky = (cislo % 100) // 10
    jednotky = cislo % 10
    text = ""

    if desetitisice > 0:
        text += desetitisicovkove[desetitisice] + " "
    if tisice > 0:
        text += tisicovkove[tisice] + " "
    if stovky > 0:
        text += stovkove[stovky] + " "
    if desitky == 1 and jednotky > 0:
        text += desetvicedodvaceti[jednotky] + " "
    else:
        if desitky > 0:
            text += desitkove[desitky] + " "
        if jednotky > 0 or (stovky == 0 and desitky == 0):
            text += jednotkove[jednotky] + " "
    print("Číslo na text:", text.strip())