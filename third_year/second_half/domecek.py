import tkinter 

def vykresli_domecek(canvas):
    canvas.create_line(
        100, 200,  
        100, 400,  
        300, 400,  
        300, 200,  
        200, 100, 
        100, 200,  
        width=2, fill="black"
    )
    canvas.create_text(200, 450, text="Můj domeček", font=("Arial", 20), fill="black")

root = tkinter.Tk()
root.title("Domeček")
canvas = tkinter.Canvas(root, width=400, height=500, bg="white")
canvas.pack()
vykresli_domecek(canvas)
root.mainloop()
