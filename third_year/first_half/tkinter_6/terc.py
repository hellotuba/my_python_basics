import tkinter

def draw_aimtest( canvas, x, y, scale ):
    canvas.create_oval( x - 50*scale, y - 50*scale, x + 50*scale, y + 50*scale, fill='white', outline='black' )
    canvas.create_oval( x - 45*scale, y - 45*scale, x + 45*scale, y + 45*scale, fill='white', outline='black' )
    canvas.create_oval( x - 40*scale, y - 40*scale, x + 40*scale, y + 40*scale, fill='black', outline='black' )
    canvas.create_oval( x - 35*scale, y - 35*scale, x + 35*scale, y + 35*scale, fill='black', outline='white' )
    canvas.create_oval( x - 30*scale, y - 30*scale, x + 30*scale, y + 30*scale, fill='blue', outline='black' )
    canvas.create_oval( x - 25*scale, y - 25*scale, x + 25*scale, y + 25*scale, fill='blue', outline='black' )
    canvas.create_oval( x - 20*scale, y - 20*scale, x + 20*scale, y + 20*scale, fill='red', outline='black' )
    canvas.create_oval( x - 15*scale, y - 15*scale, x + 15*scale, y + 15*scale, fill='red', outline='black' )
    canvas.create_oval( x - 10*scale, y - 10*scale, x + 10*scale, y + 10*scale, fill='yellow', outline='black' )
    canvas.create_oval( x - 5*scale, y - 5*scale, x + 5*scale, y + 5*scale, fill='yellow', outline='black' )

def main():
    root = tkinter.Tk()
    root.title("Aim Teste")
    canvas = tkinter.Canvas(root, width=400, height=400, bg='lightgrey')
    canvas.pack()
    draw_aimtest( canvas, 200, 200, 3.5 )
    tkinter.mainloop()

if __name__ == "__main__":
    main()