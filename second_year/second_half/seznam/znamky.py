# umožní zadat libovolný počet známek, vypočítá průměr, zobrazí nejvyšší a nejnižší známku, a vypíše, kolik známek bylo jedniček.
jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej příjmení: ")
jmeno = jmeno.capitalize()
prijmeni = prijmeni.capitalize()
znamky = input("Zadej známky oddělované čárkou: ").split(",")
znamky = [int(znamka.strip()) for znamka in znamky if znamka.strip().isdigit()]
znamky = [z for z in znamky if 1 <= z <= 5]
if not znamky:
    print(" ")
    print("ERROR: ŠPATNÉ ZNÁMKY - ZADEJTE ZNÁMKY OD 1 DO 5")
    print(" ")
else:
    prumer = sum(znamky) / len(znamky)
    nejvyssi_znamka = max(znamky)
    nejnizsi_znamka = min(znamky)
    jednicky = znamky.count(1)
    if prumer > 4.50:
        print(" ")
        print(f"> {jmeno} {prijmeni} - NEPROSPĚL")
        print(" ")
        print(f"> Průměrná známka: {prumer:.2f}")
        print(" ")
        print(f"> Nejvyšší známka: {nejvyssi_znamka}")
        print(" ")
        print(f"> Nejnižší známka: {nejnizsi_znamka}")
        print(" ")
        print(f"> Počet jedniček: {jednicky}")
    else:
        print(f"> {jmeno} {prijmeni} - PROSPĚL")
        print(" ")
        print(f"> Průměrná známka: {prumer:.2f}")
        print(" ")
        print(f"> Nejvyšší známka: {nejvyssi_znamka}")
        print(" ")
        print(f"> Nejnižší známka: {nejnizsi_znamka}")
        print(" ")
        print(f"> Počet jedniček: {jednicky}")
