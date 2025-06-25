#napiste program ktery v textu nahradi kazde druhe pismeno pismenem "X"

text = input("Zadej text: ")

if len(text) < 2:
    print("ERROR: Zadejte text s alespon 2 znaky")
else:
    text = ''.join('X' if i % 2 != 0 else char for i, char in enumerate(text))
    print("Vysledek: ", text)