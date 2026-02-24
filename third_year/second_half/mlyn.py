import tkinter

def vykresli_mlyn(canvas):
    canvas.create_rectangle(50, 50, 350, 350, outline="black", fill="yellow", width=2)
    canvas.create_rectangle(100, 100, 300, 300, outline="black", fill="yellow", width=2)
    canvas.create_rectangle(150, 150, 250, 250, outline="black", fill="yellow", width=2)
    # Vykreslení čar mlýnku
    canvas.create_line(200, 50, 200, 150, fill="black", width=2)
    canvas.create_line(200, 250, 200, 350, fill="black", width=2)
    canvas.create_line(50, 200, 150, 200, fill="black", width=2)
    canvas.create_line(250, 200, 350, 200, fill="black", width=2)
    # Vykreslení teček na křižování
    krizeni = [(200, 50), (200, 100), (200, 150), (200, 250), (200, 300), (200, 350),
                 (50, 200), (100, 200), (150, 200), (250, 200), (300, 200), (350, 200)]
    rohy = [(50, 50), (350, 50), (50, 350), (350, 350),
             (100, 100), (300, 100), (100, 300), (300, 300),
             (150, 150), (250, 150), (150, 250), (250, 250)]
    for x, y in krizeni + rohy:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")
    canvas.create_text(200, 375, text="Hra Mlýnek", font=("Arial", 20), fill="black")

root = tkinter.Tk()
root.title("Mlýnek")
canvas = tkinter.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
vykresli_mlyn(canvas)
root.mainloop()