import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Rameček")
canvas = tk.Canvas(root)
canvas.create_rectangle(40, 20, 50, 240, fill="blue")
canvas.create_rectangle(50, 20, 310, 30, fill="red")
canvas.create_rectangle(310, 20, 320, 240, fill="blue")
canvas.create_rectangle(50, 230, 310, 240, fill="red")
canvas.pack()
root.mainloop()