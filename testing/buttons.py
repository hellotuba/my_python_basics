import tkinter
from random import *

root = tkinter.Tk()
root.title("Button Example")

canvas = tkinter.Canvas(root, width=400, height=300)
canvas.pack(pady=10)

def ctverec(x,y,info):
    canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="lightblue", outline="blue", width=2)
    canvas.create_text(x, y, text=info, font=("Arial", 12, "bold"))

def kolecko(x,y,info):
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="green", outline="darkgreen", width=2)
    canvas.create_text(x, y, text=info, font=("Arial", 12, "bold"))

def button1_klik():
    ctverec(randint(20, 380), randint(20, 280), "jed")

def button2_klik():
    kolecko(randint(20, 380), randint(20, 280), "dva")

freme = tkinter.Frame(root)
freme.pack(pady=10)

button1 = tkinter.Button(freme, text="ctverec", command=button1_klik)
button1.grid(row=0, column=0, padx=10)
button2 = tkinter.Button(freme, text="kolecko", command=button2_klik)
button2.grid(row=0, column=1, padx=10) 

# start the Tk event loop
root.mainloop()

