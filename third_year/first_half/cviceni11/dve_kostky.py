import random

for i in range(5):
    def prvni_kostka():
        return random.randint(1, 6)

    def druha_kostka():
        return random.randint(1, 6)

    if __name__ == "__main__":
        kostka1 = prvni_kostka()
        kostka2 = druha_kostka()
        print(f"Hod první kostkou: {kostka1}")
        print(f"Hod druhou kostkou: {kostka2}")
        print(f"Součet hodů: {kostka1 + kostka2}")
        print("  ")