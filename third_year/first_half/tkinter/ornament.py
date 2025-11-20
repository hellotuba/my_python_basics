import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.create_rectangle(50, 10, 90, 50)
canvas.create_rectangle(150, 50, 190, 90)
canvas.create_rectangle(110, 150, 150, 190)
canvas.create_rectangle(10, 110, 50, 150)
canvas.create_rectangle(50, 50, 150, 150)
canvas.pack()
root.mainloop()