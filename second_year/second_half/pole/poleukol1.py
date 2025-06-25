pole_cisla = [1, 2, 3, 4, 5, 6]

print(pole_cisla[0])  # První prvek pole

pole_smes = [2, "želva", 2.59, 'pravda']
print(pole_smes[1])  # Druhý prvek pole

# sečti čísla v poli smes a zobraz
print(pole_smes[0] + pole_smes[2])  # Sečtení prvního a třetího prvku pole

pole_r = list(range(5))
print(pole_r)  # Vytvoření pole s hodnotami od 0 do 4

#pole pomoci for
pole_f = []
for i in range(5):  
    pole_f.append(i)  # Přidání hodnoty do pole
print(pole_f)  # Zobrazení pole

# program ctverec cisel  pocet cisel zada uzivatel
ctverec = []  # Inicializace prázdného pole
pocet = int(input("Zadej počet čísel: "))  # Získání počtu čísel od uživatele
for i in range(pocet):
    radek = list(range(pocet))
    ctverec.append(radek)  # Přidání řádku do pole
for radek in ctverec:
    print(radek)  # Zobrazení čtverce jako horizontální seznamy