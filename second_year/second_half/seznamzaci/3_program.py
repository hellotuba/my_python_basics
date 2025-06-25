# Máte seznam Ovoce. Vytvořte nový seznam, který bude obsahovat všechny druhy ovoce ze seznamu Ovoce, které začínají na např.: „b“. K zapsání podmínky můžete použít metodu startswith().
Ovoce = input("Zadejte druhy ovoce oddělené čárkou: ").split(",")
vyhledat = input("Zadejte písmeno, na které má začínat ovoce: ")
Ovoce_b = [x for x in Ovoce if x.startswith(vyhledat)]
print(Ovoce_b)