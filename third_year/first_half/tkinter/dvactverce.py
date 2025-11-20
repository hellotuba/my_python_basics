import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.create_rectangle(40, 20, 140, 110,)
canvas.create_rectangle(210, 20, 310, 110,)
canvas.pack()
root.mainloop()