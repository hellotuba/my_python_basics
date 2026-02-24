import tkinter
from random import *
canvas = tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

def sipka_nahoru(event):
    x=randrange(300)
    y=randrange(250)
    canvas.create_line(x-10, y+20, x, y, x+10, y+20)
    canvas.create_line(x, y, x, y+40)

def sipka_dolu(event):
    x=randrange(300)
    y=randrange(250)
    canvas.create_line(x-10, y+20, x, y+40, x+10, y+20)
    canvas.create_line(x, y, x, y+40)

def sipka_doprava(event):
    x = randrange(300)
    y = randrange(250)
    canvas.create_line(x, y-10, x+20, y, x, y+10)
    canvas.create_line(x, y, x+10, y)

def sipka_doleva(event):
    x = randrange(300)
    y = randrange(250)
    canvas.create_line(x, y-10, x-20, y, x, y+10)
    canvas.create_line(x, y, x-10, y)

canvas.bind_all('<Up>', sipka_nahoru)
canvas.bind_all('<Down>', sipka_dolu)
canvas.bind_all('<Right>', sipka_doprava)
canvas.bind_all('<Left>', sipka_doleva)
tkinter.mainloop()
