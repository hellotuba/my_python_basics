import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Finsko")
canvas = tk.Canvas(root)
canvas.create_rectangle(40, 20, 320, 200, fill="white")
canvas.create_rectangle(120, 20, 160, 200, fill="blue", outline="")
canvas.create_rectangle(40, 90, 320, 130, fill="blue", outline="")
canvas.pack()
root.mainloop()