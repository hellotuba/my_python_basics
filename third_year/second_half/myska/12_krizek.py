import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kriz(souradnice):
    x = souradnice.x
    y = souradnice.y
    canvas.create_line(x-5, y-5, x+5, y+5, fill="red")
    canvas.create_line(x-5, y+5, x+5, y-5, fill="red")

canvas.create_text(190, 10, text="Klikni myší pro křížek", fill="black")
canvas.bind("<Button-1>", kriz)
canvas.mainloop()