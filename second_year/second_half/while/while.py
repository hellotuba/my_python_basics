#i = 1
#while i<=5:
#    print(i)
#    i+=1 #zvýšní o 1

# Program se zepta na heslo uzivatele dokud nezada spravne heslo nono to dal :D po zadani spravneho hesla dostane konfety "Přístup povolen🎉"

heslo = str(input("Zadejte Heslo (LOW-BASED-SECURITY): "))
realheslo = "HDA7SdwsdD051"
while heslo != realheslo:
    print("Špatné heslo")
    heslo = input("Zadejte heslo znovu: ")

print("Přístup povolen🎉")