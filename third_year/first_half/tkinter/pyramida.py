import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.create_rectangle(150, 50, 200, 100)
canvas.create_rectangle(100, 100, 250, 150)
canvas.create_rectangle(50, 150, 300, 200)
canvas.pack()
root.mainloop()