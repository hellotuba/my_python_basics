import tkinter as tk

okno = tk.Tk()
okno.title("Deformace")
canvas = tk.Canvas(okno, width=400, height=400, bg="white")
canvas.pack()

puvodni_vlastnosti = {}

def ctverecmodry():
    return canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="blue")

def zelenekolo():
    return canvas.create_oval(200, 50, 300, 150, fill="green", outline="green")

def zlutykolo():
    return canvas.create_oval(50, 200, 150, 300, fill="yellow", outline="yellow")

def cervenyctverec():
    return canvas.create_rectangle(200, 200, 300, 300, fill="red", outline="black")

def whiteroof():
    return canvas.create_polygon(50, 350, 150, 350, 100, 300, fill="white", outline="black")

def orangeroof():
    return canvas.create_polygon(200, 350, 300, 350, 250, 300, fill="orange", outline="orange")

def textnaobrat():
    return canvas.create_text(200, 25, text="Vlastnosti útvarů", font=("Arial", 20))

utvary = [ctverecmodry(), zelenekolo(), zlutykolo(), cervenyctverec(), whiteroof(), orangeroof(), textnaobrat()]
for utvar in utvary:
    puvodni_vlastnosti[utvar] = {
        "coords": canvas.coords(utvar),
        "fill": canvas.itemcget(utvar, "fill")
    }
    if canvas.type(utvar) != "text":
        puvodni_vlastnosti[utvar]["outline"] = canvas.itemcget(utvar, "outline")

def zmensit():
    for utvar in utvary:
        bbox = canvas.bbox(utvar)
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            canvas.scale(utvar, (x1 + x2) / 2, (y1 + y2) / 2, 0.7, 0.7)

def otocittext():
    for utvar in utvary:
        if isinstance(utvar, int) and canvas.type(utvar) == "text":
            canvas.itemconfigure(utvar, text="Vlastnosti útvarů"[::-1], font=("Arial", 20))

tlacitka = tk.Frame(okno)
tlacitka.pack()
tk.Button(tlacitka, text="Zmenšit všechny útvary", command=zmensit).pack(side=tk.LEFT, padx=5)
tk.Button(tlacitka, text="otocit text", command=otocittext).pack(side=tk.LEFT, padx=5)

okno.mainloop()