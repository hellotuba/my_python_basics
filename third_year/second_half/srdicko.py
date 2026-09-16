from tkinter import *

def kresli(mys):
    canvas.create_line(150, 100, mys.x, mys.y, fill='red', width=2)

root = Tk()
canvas = Canvas(root, width=400, height=400, bg='white')
canvas.pack()
canvas.bind('<B1-Motion>', kresli)  # Changed from <B1-Motion> to <Motion>
root.mainloop()
