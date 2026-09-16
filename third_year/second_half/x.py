import tkinter
canvas = tkinter.Canvas(bg="black", width=520, height=520)
canvas.pack()

def draw_x(x, y):
    canvas.create_line(x-10, y-10, x+10, y+10, fill="white", width=2)
    canvas.create_line(x-10, y+10, x+10, y-10, fill="white", width=2)

spacing = 20  # nospace
spaccing = 40  # space

def nospace(x, y):
    for row in range(1):
        for col in range(10):
            x = col * spacing + 10
            y = row * spacing + 10
            if x < 520 and y < 520:
                draw_x(x, y)
                canvas.update()
                canvas.after(50)

def space(x, y):
    for row in range(1):
        for col in range(10):
            x = col * spaccing + 10
            y = row * spaccing + 10
            if x < 520 and y < 520:
                draw_x(x, y)
                canvas.update()
                canvas.after(50)

nospace(10, 10)
canvas.after(1000)  # wait for 1s
canvas.delete("all")
space(10, 40)
canvas.mainloop()
