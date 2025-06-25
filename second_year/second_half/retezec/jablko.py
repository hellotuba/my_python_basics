# vytvorte program ktery prevede zadany text na velka pismena a jednotlive pismena oddeli zadanym znakem
text = input("Zadejte text: ")
separator = input("Zadejte oddelovac: ")
text_upper = text.upper()
if text == "":
    print("Text nesmí být prázdný.")
elif separator == "":
    print("Oddělovač nesmí být prázdný.")
else:
    result = separator.join(text_upper)
    print("Výsledek:", result)