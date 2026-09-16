# spedliky
from tkinter import *
def kresli(mys):
    canvas.create_oval(mys.x-5, mys.y-5, mys.x+5, mys.y+5, fill='red', outline='red')
    canvas.create_line(mys.x, mys.y+5, mys.x, mys.y+25, fill='black')

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', kresli)
root.mainloop()