import random

seznam = [random.randint(1, 100) for _ in range(50)]
print("Seznam čísel:", *seznam)

pocet_vyskytu = {}

for cislo in seznam:
    if cislo in pocet_vyskytu:
        pocet_vyskytu[cislo] += 1
    else:
        pocet_vyskytu[cislo] = 1

nejcastejsi_cislo = max(pocet_vyskytu, key=pocet_vyskytu.get) # vezme nejvyssi hodnotu
nejvyssi_pocet = pocet_vyskytu[nejcastejsi_cislo]

print(f"Nejčastější číslo je {nejcastejsi_cislo} a vyskytuje se {nejvyssi_pocet} krát.")
