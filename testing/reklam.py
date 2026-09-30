# vytvorte program ve kterem uzivatel zada slovo toto slovo se v tkinteru na canvas vypise v podobe "reklamniho napisu" kde kazdy znak zadaneho slova bude vypany nahodne vybranou barvou 

import random
import tkinter

def draw_text(canvas, text):
    canvas.delete("all") 
    colors = ["#FF1744", "#FFEA00", "#00E676", "#00B0FF", "#D500F9"]
    x = 20
    y = 50 

    for char in text:
        color = random.choice(colors)
        canvas.create_text(x, y, text=char, fill=color, font=("Helvetica", 32))
        x += 30  


root = tkinter.Tk()
root.title("Reklamní nápis")
root.configure(bg="#F3F4F6")

frame = tkinter.Frame(root, bg="#F3F4F6", padx=20, pady=20)
frame.pack()

entry1 = tkinter.Entry(
    frame,
    width=15,
    font=("Arial", 12),
    bg="white",
    fg="#111827",
    relief="flat",
)
entry1.grid(row=0, column=1, pady=5, padx=5)

canvas = tkinter.Canvas(
    frame,
    width=500,
    height=100,
    bg="white",
    highlightthickness=0,
)
canvas.grid(row=1, column=0, columnspan=2, pady=10)

button = tkinter.Button(
    frame,
    text="Zobrazit",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=12,
    pady=5,
    command=lambda: draw_text(canvas, entry1.get()),
)
button.grid(row=2, column=0, padx=(0, 5), pady=10)

button = tkinter.Button(
    frame,
    text="Smazat",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=12,
    pady=5,
    command=lambda: canvas.delete("all"),
)
button.grid(row=2, column=1, padx=(5, 0), pady=10)

root.bind("<Return>", lambda event: draw_text(canvas, entry1.get()))
root.mainloop()