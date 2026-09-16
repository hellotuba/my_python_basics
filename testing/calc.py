import tkinter
from random import *

root = tkinter.Tk()
canvas = tkinter.Canvas()
canvas.pack()

def secti(info):
    canvas.delete("answer")
    canvas.create_text(20, 200, text=info, tag="answer")

def button4_click():
    cislo1 = int(entry1.get())
    cislo2 = int(entry2.get())
    secti(cislo1 + cislo2)

def button5_click():
    cislo1 = int(entry1.get())
    cislo2 = int(entry2.get())
    secti(cislo1 - cislo2)

def button6_click():
    cislo1 = int(entry1.get())
    cislo2 = int(entry2.get())
    secti(cislo1 * cislo2)

def button7_click():
    cislo1 = int(entry1.get())
    cislo2 = int(entry2.get())
    secti(cislo1 / cislo2)

button4 = tkinter.Button(text="Sčítání", command=button4_click)
button4.pack()

button5 = tkinter.Button(text="Odčítání", command=button5_click)
button5.pack()

button6 = tkinter.Button(text="Násobení", command=button6_click)
button6.pack()

button7 = tkinter.Button(text="Dělení", command=button7_click)
button7.pack()

entry1 = tkinter.Entry()
entry1.pack()

entry2 = tkinter.Entry()
entry2.pack()

root.mainloop()