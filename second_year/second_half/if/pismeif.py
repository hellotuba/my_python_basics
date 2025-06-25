mojepismenko = ["A", "B", "C"]
pismenko = str(input("Zadejte písmeno: "))

if pismenko.upper() in mojepismenko:
    print("Uhádl si písmenko! 🎉")
else:
    print("Bohužel si písmenko neuhádl 😔")