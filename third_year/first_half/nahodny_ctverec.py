import tkinter as tk
import random

def create_random_square():
    root = tk.Tk()
    canvas_size = 400
    square_size = 50
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()

    x1 = random.randint(0, canvas_size - square_size)
    y1 = random.randint(0, canvas_size - square_size)
    x2 = x1 + square_size
    y2 = y1 + square_size

    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    root.mainloop()

if __name__ == "__main__":
    create_random_square()
