K = int(input("Zadejte K: "))
N = int(input("Zadejte N: "))

for i in range(K - K, N):
    print(i, end=" ")
    if i == N - 1:
        print("*", end=" ")

for i in range(N, N + 2):  # Vytiskne N a N+1
    print(i, end=" ")

print()