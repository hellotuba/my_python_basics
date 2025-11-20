import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Nizozemsko")
canvas = tk.Canvas(root)
canvas.create_rectangle(40, 20, 360, 90, fill="red")
canvas.create_rectangle(40, 90, 360, 160, fill="white")
canvas.create_rectangle(40, 160, 360, 240, fill="blue")
canvas.pack()
root.mainloop()