# 1. Napište program, který vezme seznam čísel num_list a vrátí seznam těch čísel ze seznamu, která jsou dělitelná číslem n (v původním pořadí). Číslo n bude zadávat uživatel od 1 do 10.
import random

num_list = [random.randint(1, 100) for _ in range(50)]
n = int(input("Zadejte číslo od 1 do 10: "))
if n > 10:
    print("Číslo není v požadovaném rozsahu od 1 do 10.")
elif n == 0: # HANDLER FOR ZERO
    print("Nulou nelze dělit.")
elif n < 0: # HANDLER FOR NEGATIVE NUMBERS
    print("Záporným číslem nelze dělit.")
else:
    div_nums = [num for num in num_list if num % n == 0]
    print("Čísla dělitelná číslem", n, "jsou:", div_nums)