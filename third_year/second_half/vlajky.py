import tkinter as tk

root = tk.Tk()
root.title("Vlajky binds")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

def norsko(event):
    RED = "#BA0C2F"
    WHITE = "#FFFFFF"
    BLUE = "#00205B"

    canvas.create_rectangle(0, 0, 600, 400, fill=RED, outline="")
    canvas.create_rectangle(0, 150, 600, 250, fill=WHITE, outline="")
    canvas.create_rectangle(200, 0, 300, 400, fill=WHITE, outline="")
    canvas.create_rectangle(0, 170, 600, 230, fill=BLUE, outline="")
    canvas.create_rectangle(220, 0, 280, 400, fill=BLUE, outline="")

def cesko(event):
    WHITE = "white"
    RED = "red"
    BLUE = "blue"

    canvas.create_rectangle(0, 0, 600, 400, fill=WHITE, outline="")
    canvas.create_rectangle(0, 200, 600, 400, fill=RED, outline="")
    canvas.create_polygon(0, 0, 300, 200, 0, 400, fill=BLUE, outline="")

def finsko(event):
    WHITE = "white"
    BLUE = "blue"

    canvas.create_rectangle(0, 0, 600, 400, fill=WHITE, outline="")
    canvas.create_rectangle(0, 150, 600, 250, fill=BLUE, outline="")
    canvas.create_rectangle(200, 0, 300, 400, fill=BLUE, outline="")

def clear(event=None):
    canvas.delete("all")

canvas.bind_all('<n>', norsko)
canvas.bind_all('<c>', cesko)
canvas.bind_all('<f>', finsko)
canvas.bind_all('<Delete>', clear)
root.mainloop()
