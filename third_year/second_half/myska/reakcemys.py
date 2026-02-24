import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def krouzek(souradnice):
    x = souradnice.x
    y = souradnice.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")

def dum(souradnice):
    x = souradnice.x
    y = souradnice.y
    canvas.create_rectangle(x, y, x+50, y+50, fill="blue")
    canvas.create_line(x, y, x+25, y-50, x+50, y)

canvas.bind("<Button-1>", krouzek)
canvas.bind("<Button-3>", dum)
canvas.mainloop()