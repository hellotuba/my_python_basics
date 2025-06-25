# Napište program ABECEDA, který vypíše prvních n písmen anglické abecedy. Pokud je n větší jak 26, písmena jsou vypisována opakovaně.
n = int(input("Zadejte počet písmen abecedy (n): "))
abeceda = "abcdefghijklmnopqrstuvwxyz"
fin_abeceda = abeceda.upper()  # Převod abecedy na velká písmena 
if n <= 0:
    print("Zadejte kladné číslo.")
else:
    vysledek = ""
    for i in range(n):
        vysledek += fin_abeceda[i % 26]
    anone = input("Chcete výsledek v malých nebo velkých písmenech (mal/vel): ")
    if anone == "mal":
        vysledek = vysledek.lower()
    elif anone == "vel":
        vysledek = vysledek.upper()
    else:
        print("NEPLATNÁ VOLBA! výchozí je velká písmena.")
        vysledek = vysledek.upper()
    print("Výsledek:", vysledek)
