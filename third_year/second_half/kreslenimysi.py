# kreselni pomoci mysi
# '<B1-Motion>' - pohyb mysi s drzenim leveho tlacitka
from tkinter import *
def kresli(event):
    x = event.x
    y = event.y 
    canvas.create_oval(x-5, y-5, x+5, y+5, fill='black')

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', kresli)
root.mainloop()
