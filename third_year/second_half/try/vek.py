try:
    vek = int(input("Zadej svůj věk: "))
    print(f"Za 10 let ti bude {vek + 10} let.")
except ValueError:
    print("Upozornění: Zadej prosím číslo, ne text!")