import tkinter 
import random

def hvezdicka(platno, x, y):
    sirka = 2
    vyska = 2
    platno.create_rectangle(x , y - vyska, x  + sirka, y, fill="yellow", outline="yellow")

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Obloha s hvězdičkami")
    platno = tkinter.Canvas(root, width=550, height=350, bg="navy")
    platno.pack()
    
    positions = [(random.randint(0, 550), random.randint(0, 350)) for _ in range(1000)]

    
    for x, y in positions:
        hvezdicka(platno, x, y)
    
    root.mainloop()