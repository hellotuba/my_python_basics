import tkinter
import random

def hod_kostkama():
    kostrka1 = random.randint(1, 6)
    return [kostrka1]

def kosticky(platno, x, y):
    kostky = hod_kostkama()
    kostka_sirka = 55
    kostka_vyska = 55
    for index, hodnota in enumerate(kostky):
        x_pos = x + index * (kostka_sirka + 10)
        platno.create_rectangle(x_pos, y, x_pos + kostka_sirka, y + kostka_vyska, fill="white", outline="black")
        platno.create_text(x_pos + kostka_sirka / 2, y + kostka_vyska / 2, text=str(hodnota), font=("Arial", 50))

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Kostky s čísly")
    platno = tkinter.Canvas(root, width=550, height=350, bg="navy")
    platno.pack()
    
    for _ in range(5):
        x = random.randint(0, 520)
        y = random.randint(0, 320)
        kosticky(platno, x, y)
    
    root.mainloop()