# Vstupem v této úloze je table, což je seznam seznamů čísel reprezentujících tabulku čísel. Napište program Sloupec, který vypíše součty hodnot v jednotlivých sloupcích.
tabulka = [[1,4], [2,3]]

def sloupec_soucet(tabulka):
    if not tabulka or not tabulka[0]:
        return []

    num_columns = len(tabulka[0])
    column_sums = [0] * num_columns

    for i in range(num_columns):
        column_sums[i] = sum(row[i] for row in tabulka)

    return column_sums

soucet = sloupec_soucet(tabulka)
print("Součty hodnot v jednotlivých sloupcích jsou:", soucet)
