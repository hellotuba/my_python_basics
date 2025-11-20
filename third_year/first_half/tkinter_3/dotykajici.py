import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 150, 150, fill="red")
canvas.create_rectangle(150, 150, 250, 250, fill="blue")
canvas.create_rectangle(250, 50, 350, 150, fill="green")
root.mainloop()