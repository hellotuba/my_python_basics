def encrypt(word, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_word = ''
    
    for char in word:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            index = (letters.index(char.lower()) + key) % 26
            encrypted_word += letters[index].upper() if char.isupper() else letters[index]
        else:
            encrypted_word += char
            
    return encrypted_word

def decrypt(word, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_word = ''
    
    for char in word:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            index = (letters.index(char.lower()) - key) % 26
            decrypted_word += letters[index].upper() if char.isupper() else letters[index]
        else:
            decrypted_word += char
            
    return decrypted_word

question = input("Chcete Encryptovat (encrypt) nebo Decryptovat (decrypt): ")
word = input("Zadejte slovo: ")
key = int(input("Zadejte pozici (číslo): "))
if question.lower() == 'encrypt':  # Check for 'encrypt' string
    print("Zašifrované slovo:", encrypt(word, key))
elif question.lower() == 'decrypt':  # Check for 'decrypt' string
    print("Dešifrované slovo:", decrypt(word, key))
else:
    print("Neplatná volba. Zadejte 'encrypt' nebo 'decrypt'.")
