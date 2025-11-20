import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Přes sebe")
canvas = tk.Canvas(root)
canvas.create_rectangle(50, 20, 200, 170, fill="purple")
canvas.create_rectangle(80, 50, 230, 200, fill="hotpink")
canvas.create_rectangle(110, 80, 260, 230, fill="pink")
canvas.create_rectangle(140, 110, 290, 260, fill="salmon")
canvas.pack()
root.mainloop()