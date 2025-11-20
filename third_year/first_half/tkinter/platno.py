import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root, background="gray")
canvas.create_rectangle(20, 20, 110, 110, fill="blue")
canvas.create_rectangle(250, 250, 160, 160)
canvas.pack()
root.mainloop()