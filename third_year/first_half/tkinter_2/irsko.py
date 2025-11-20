import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Irsko")
canvas = tk.Canvas(root)
canvas.create_rectangle(40, 20, 120, 200, fill="green")
canvas.create_rectangle(120, 20, 240, 200, fill="white")
canvas.create_rectangle(240, 20, 320, 200, fill="orange")
canvas.pack()
root.mainloop()