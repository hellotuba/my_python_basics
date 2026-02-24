import tkinter
from random import *
canvas = tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

def default():
    canvas.create_text(400, 100, text="h = hello world! \n b = bye bye \n g = good evening \n c = clear \n m = good morning", font=("Arial", 24), fill="black")

def bye(event):
    canvas.create_text(400, 300, text="Bye bye!", font=("Arial", 24), fill="black")

def helo(event):
    canvas.create_text(400, 300, text="Hello, World!", font=("Arial", 24), fill="black")

def wsp(event):
    canvas.create_text(400, 300, text="Good evening!", font=("Arial", 24), fill="black")

def clear(event):
    canvas.delete("all")
    default()

def mornin(event):
    canvas.create_text(400, 300, text="Good morning!", font=("Arial", 24), fill="black")

canvas.bind_all('<b>', bye)
canvas.bind_all('<h>', helo)
canvas.bind_all('<g>', wsp)
canvas.bind_all('<m>', mornin)
canvas.bind_all('<c>', clear)
default()
tkinter.mainloop()
