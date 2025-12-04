import tkinter

def draw_snowman( canvas, x, y, scale ):
    canvas.create_oval( x - 30*scale, y - 30*scale, x + 30*scale, y + 30*scale, fill='white', outline='black' )  
    canvas.create_oval( x - 20*scale, y - 70*scale, x + 20*scale, y - 10*scale, fill='white', outline='black' )  
    canvas.create_oval( x - 15*scale, y - 100*scale, x + 15*scale, y - 70*scale, fill='white', outline='black' ) 
    canvas.create_oval( x - 5*scale, y - 90*scale, x - 1*scale, y - 86*scale, fill='black' ) 
    canvas.create_oval( x + 1*scale, y - 90*scale, x + 5*scale, y - 86*scale, fill='black' )  
    canvas.create_polygon( x, y - 80*scale, x - 5*scale, y - 75*scale, x + 5*scale, y - 75*scale, fill='orange' )  
    canvas.create_line( x - 10*scale, y - 60*scale, x + 10*scale, y - 60*scale, fill='black' )  
    canvas.create_line( x - 20*scale, y - 40*scale, x - 40*scale, y - 20*scale, fill='brown', width=3 )  
    canvas.create_line( x + 20*scale, y - 40*scale, x + 40*scale, y - 20*scale, fill='brown', width=3 )  

def main():
    root = tkinter.Tk()
    root.title("lil snowman")
    canvas = tkinter.Canvas(root, width=400, height=400, bg='lightblue')
    canvas.pack()
    draw_snowman( canvas, 200, 300, 2 )
    tkinter.mainloop()

if __name__ == "__main__":
    main()