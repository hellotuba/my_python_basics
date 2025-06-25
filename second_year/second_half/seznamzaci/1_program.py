# Máte seznam čísel pojmenovaný Nums. Chcete vytvořit nový seznam, který bude obsahovat třetí mocninu všech čísel v seznamu Nums.
Nums = input("Zadej seznam čísel oddělených čárkou: ")
Nums = Nums.split(",")
mocni = [int(x)**3 for x in Nums]
print(mocni)