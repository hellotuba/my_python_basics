#Napište program Nej_slovo, který najde nejdelší slovo ze zadaného seznamu slov. Pokud je nejdelších slov více, zobrazí to z nich, které je v seznamu uvedeno jako první.
slova = input("Zadejte seznam slov oddělených čárkou: ").split(",")
nejdelsi_slovo = ""
for slovo in slova:
    if len(slovo) > len(nejdelsi_slovo):
        nejdelsi_slovo = slovo.strip()
print("Nejdelší slovo je:", nejdelsi_slovo)