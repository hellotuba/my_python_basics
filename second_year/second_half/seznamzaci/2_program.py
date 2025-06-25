# Máte seznam Autor = ["karel čapek","bohumil hrabal","vladimír páral","halina pavlowská"]. Pomocí metody str.title() vytvořte nový seznam Autor_N, příklad: Karel Čapek.
Autor = input("Zadejte autory oddělené čárkou: ").split(",")
Autor_N = [x.title() for x in Autor]
print(Autor_N)