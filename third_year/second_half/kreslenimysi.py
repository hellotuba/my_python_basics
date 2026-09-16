# kreselni pomoci mysi
# '<B1-Motion>' - pohyb mysi s drzenim leveho tlacitka
# rozdelit na 4 ctvrtiny a kreslit ruzne barvy 
from tkinter import *
def kresli(mys):
    if mys.x < 200 and mys.y < 200:
        barva = 'red'
    elif mys.x >= 200 and mys.y < 200:
        barva = 'green'
    elif mys.x < 200 and mys.y >= 200:
        barva = 'blue'
    else:
        barva = 'yellow'
    canvas.create_rectangle(mys.x-5, mys.y-5, mys.x+5, mys.y+5, fill=barva, outline=barva)

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', kresli)
root.mainloop()
