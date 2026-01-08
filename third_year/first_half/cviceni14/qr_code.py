import tkinter
import random

def qr_code(platno, x, y, velikost):
    for corner_x, corner_y in [(0, 0), (14, 0), (0, 14)]:
        for i in range(7):
            for j in range(7):
                platno.create_rectangle(x + (corner_x + i) * velikost, y + (corner_y + j) * velikost, x + (corner_x + i + 1) * velikost, y + (corner_y + j + 1) * velikost, fill="black", outline="black")
        for i in range(1, 6):
            for j in range(1, 6):
                platno.create_rectangle(x + (corner_x + i) * velikost, y + (corner_y + j) * velikost, x + (corner_x + i + 1) * velikost, y + (corner_y + j + 1) * velikost, fill="white", outline="white")
        for i in range(2, 5):
            for j in range(2, 5):
                platno.create_rectangle(x + (corner_x + i) * velikost, y + (corner_y + j) * velikost, x + (corner_x + i + 1) * velikost, y + (corner_y + j + 1) * velikost, fill="black", outline="black")
                
    for i in range(8, 13):
        color = "black" if i % 2 == 0 else "white"
        platno.create_rectangle(x + i * velikost, y + 6 * velikost, x + (i + 1) * velikost, y + 7 * velikost, fill=color, outline=color)
        platno.create_rectangle(x + 6 * velikost, y + i * velikost, x + 7 * velikost, y + (i + 1) * velikost, fill=color, outline=color)
    
    for i in range(21):
        for j in range(21):
            if (i < 9 and j < 9) or (i < 9 and j > 11) or (i > 11 and j < 9) or (i == 6) or (j == 6):
                continue
            color = "black" if random.random() > 0.5 else "white"
            platno.create_rectangle(x + i * velikost, y + j * velikost, x + (i + 1) * velikost, y + (j + 1) * velikost, fill=color, outline=color)

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("QR Code")
    platno = tkinter.Canvas(root, width=500, height=500, bg="white")
    platno.pack()
    
    qr_code(platno, 50, 50, 20)
    
    root.mainloop()