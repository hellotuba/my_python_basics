import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=250, height=250)
canvas.pack()
canvas.create_rectangle(50, 50, 200, 200, fill="lightblue")
canvas.create_rectangle(50, 50, 150, 150, fill="blue")
canvas.create_rectangle(50, 50, 100, 100, fill="darkblue")
root.mainloop()