#Vytvořte program, který ze zadaného textu odstraní nejčastější znak. Odstraní první nejčastější znak.
text = input("Zadejte text: ")
if text == "":
    print("Text nesmí být prázdný.")
else:
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    most_common_char = max(char_count, key=char_count.get)
    result = text.replace(most_common_char, "")
    print("Výsledek:", result)