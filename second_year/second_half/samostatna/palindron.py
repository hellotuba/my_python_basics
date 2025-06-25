text = input("Zadejte text: ")
palindrom = text[::-1]  # Reverzní řetězec

if text == palindrom:
    print("Text je palindrom.", palindrom)
else:   
    print("Text není palindrom.")
