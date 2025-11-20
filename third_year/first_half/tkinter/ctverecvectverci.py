import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.create_rectangle(70, 70, 130, 130)
canvas.create_rectangle(50, 50, 150, 150)
canvas.pack()
root.mainloop()