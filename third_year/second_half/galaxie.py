from random import *
import tkinter
canvas = tkinter.Canvas(bg="black", width=520, height=520)
canvas.pack()

x = 10
y = 10
for i in range(1, 26):
    x = x + 20
    y = y + 20
    canvas.create_line(x, 10, 510, y, fill="white", width=2)    # vpravo nahoře
    canvas.create_line(x, 510, 10, y, fill="white", width=2)    # vlevo dole
    canvas.create_line(520-x, 10, 10, y, fill="white", width=2)  # vlevo nahoře
    canvas.create_line(520-x, 510, 510, y, fill="white", width=2) # vpravo dole
    canvas.update()
    canvas.after(100)

canvas.mainloop()