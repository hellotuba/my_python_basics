import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def smajlik(souradnice):
    x = souradnice.x
    y = souradnice.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
    canvas.create_oval(x-15, y-15, x+15, y+15, fill="yellow")
    canvas.create_oval(x-10, y-10, x-5, y-5, fill="black")
    canvas.create_oval(x+5, y-10, x+10, y-5, fill="black")
    canvas.create_arc(x-10, y-10, x+10, y+10, start=200, extent=140, fill="black")

canvas.create_text(190, 10, text="Klikni myší pro smajlíka", fill="black")
canvas.bind("<Button-1>", smajlik)
canvas.mainloop()