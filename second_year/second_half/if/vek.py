# zada vek (podminky )
vek = int(input("Zadejte věk: "))

if vek < 6:
    print("Předškolák")
elif vek < 18:
    print("Školák")
elif vek < 60:
    print("Dospělí")
elif vek > 60:
    print("důchodce")