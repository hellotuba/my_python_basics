N = int(input("Zadejte N: "))

def print_numbers_and_sum(N):
    total_sum = 0
    for i in range(1, N + 1):
        print(i)
        total_sum += i
    print("Součet čísel od 1 do", N, "je:", total_sum)

print_numbers_and_sum(N)

N2 = int(input("Zadejte obracen N: "))

def print_numbers_and_sum_reverse(N2):
    total_sum2 = 0
    for i in range(N2, 0, -1):  
        print(i)
        total_sum2 += i
    print("Součet čísel od", N2, "do 1 je:", total_sum2)

print_numbers_and_sum_reverse(N2)