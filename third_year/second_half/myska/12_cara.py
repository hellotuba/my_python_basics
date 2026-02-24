import tkinter

canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

def carka(event):
    pozice_x = 200
    pozice_y = 280
    canvas.create_line(event.x, event.y, pozice_x, pozice_y, fill="green", width=5)

canvas.create_text(200, 20, text="Klikni myší", fill="black")
canvas.bind("<Button-1>", carka)
canvas.mainloop()
