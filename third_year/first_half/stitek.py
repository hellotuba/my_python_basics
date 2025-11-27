# stitek jmena na nahodne pozici
import random
import tkinter 
canvas_size = 700
square_size = 340
root = tkinter.Tk()
root.title("Náhodný štítek jména")
canvas = tkinter.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

def random_stitek():
    x1 = random.randint(0, canvas_size - square_size)
    y1 = random.randint(0, canvas_size - square_size)
    x2 = x1 + square_size
    y2 = y1 + 120
    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
    ox = x1 + 10
    oy = y1 + 10
    # J
    canvas.create_line(ox + 40, oy + 0, ox + 40, oy + 80, fill='black', width=3)
    canvas.create_line(ox + 40, oy + 80, ox + 20, oy + 100, fill='black', width=3)
    canvas.create_line(ox + 20, oy + 100, ox + 0, oy + 90, fill='black', width=3)
    # A
    canvas.create_line(ox + 60, oy + 100, ox + 80, oy + 0, fill='black', width=3)
    canvas.create_line(ox + 80, oy + 0, ox + 100, oy + 100, fill='black', width=3)
    canvas.create_line(ox + 70, oy + 50, ox + 90, oy + 50, fill='black', width=3)
    # K
    canvas.create_line(ox + 120, oy + 0, ox + 120, oy + 100, fill='black', width=3)
    canvas.create_line(ox + 120, oy + 50, ox + 160, oy + 0, fill='black', width=3)
    canvas.create_line(ox + 120, oy + 50, ox + 160, oy + 100, fill='black', width=3)
    # U
    canvas.create_line(ox + 180, oy + 0, ox + 180, oy + 80, fill='black', width=3)
    canvas.create_line(ox + 180, oy + 80, ox + 220, oy + 80, fill='black', width=3)
    canvas.create_line(ox + 220, oy + 80, ox + 220, oy + 0, fill='black', width=3)
    # B 
    canvas.create_line(ox + 240, oy + 0, ox + 240, oy + 100, fill='black', width=3)
    canvas.create_line(ox + 240, oy + 0, ox + 285, oy + 10, fill='black', width=3)
    canvas.create_line(ox + 285, oy + 10, ox + 285, oy + 35, fill='black', width=3)
    canvas.create_line(ox + 285, oy + 35, ox + 240, oy + 40, fill='black', width=3)
    canvas.create_line(ox + 240, oy + 40, ox + 285, oy + 50, fill='black', width=3)
    canvas.create_line(ox + 285, oy + 50, ox + 285, oy + 90, fill='black', width=3)
    canvas.create_line(ox + 285, oy + 90, ox + 240, oy + 100, fill='black', width=3)

    canvas.create_text(x1 + square_size // 2, y2 + 20, text='Jakub', font=('Arial', 30), fill='purple')

random_stitek()
root.mainloop()