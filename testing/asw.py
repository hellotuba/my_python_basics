import random

min = 1
max = 100
wins = 0

def guessing():
    global wins
    final = random.randint(min, max)
    while True:
        guess = int(input(f"Zjisti číslo mezi {min} a {max}: "))
        if guess < final:
            print("Nízko, zkus to znovu.")
        elif guess > final:
            print("Vysoko, zkus to znovu.")
        else:
            print("Gratulace! Uhodl jsi číslo.")
            wins = wins + 1
            continue_game()
            break

def continue_game():
    while True:
        answer = input("Chceš hrát znovu? (ano/ne): ").lower()
        if answer == "ano":
            guessing()
        elif answer == "ne":
            print("Díky za hraní!")
            print(f"Celkový počet výher: {wins}"    )
            rating()
            break
        else:
            print("Neplatná odpověď, zadej 'ano' nebo 'ne'.")

def rating():
    if wins >= 5:
        print("Skvělá práce! Jsi mistr hádání!")
    elif wins >= 3:
        print("Dobrá práce! Máš dobré hádací schopnosti!")
    else:
        print("Můžeš to zlepšit! Zkus to znovu a získej více výher!")


if __name__ == "__main__":
    guessing()