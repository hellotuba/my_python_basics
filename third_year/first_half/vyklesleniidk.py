import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(width=600, height=200, bg='white')
canvas.pack()
x=3
y=3
delka=200
# čára
canvas.create_line(x, y, x + delka, y, fill='red', width=3)
# trojúhelník
canvas.create_polygon(10, 100, 110, 5, 210, 100, outline='darkblue', fill='lightblue', width=3)
# Písmenka L, T, H, Z pomocí čar
# L
canvas.create_line(250, 10, 250, 110, fill='black', width=3) 
canvas.create_line(250, 110, 300, 110, fill='black', width=3) 
# T
canvas.create_line(320, 10, 320, 110, fill='black', width=3) 
canvas.create_line(270, 10, 370, 10, fill='black', width=3) 
# H
canvas.create_line(390, 10, 390, 110, fill='black', width=3) 
canvas.create_line(440, 10, 440, 110, fill='black', width=3)  
canvas.create_line(390, 60, 440, 60, fill='black', width=3)  
# Z
canvas.create_line(460, 10, 510, 10, fill='black', width=3) 
canvas.create_line(510, 10, 460, 110, fill='black', width=3)  
canvas.create_line(460, 110, 510, 110, fill='black', width=3) 

canvas.create_text(300, 150, text='Testovaci tkinter', font=('Arial', 40), fill='purple')
root.mainloop()
