text = input("Zadejte text: ")
znak = input("Zadejte písmeno které chcete vyhledat: ")
pocet = 0

for i in text:
    if i == znak or i == znak.upper() or i == znak.lower():
        pocet += 1
print("Počet výskytů písmene", znak, "v textu je:", pocet)