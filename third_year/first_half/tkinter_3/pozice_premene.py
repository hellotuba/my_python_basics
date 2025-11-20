import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 70
canvas.create_rectangle(x, y, x + 100, y + 100, fill="yellow")
root.mainloop()