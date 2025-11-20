import tkinter
def robot():
    okno = tkinter.Tk()
    okno.title("Robot")
    okno.geometry("300x400")
    canvas = tkinter.Canvas(okno, width=300, height=400, bg="white")
    canvas.pack()
    # Hlava
    canvas.create_rectangle(105, 50, 195, 125, fill="blue")
    # krk
    canvas.create_rectangle(120, 125, 180, 150, fill="lightblue")
    # Tělo
    canvas.create_rectangle(100, 150, 200, 300, fill="blue")
    # Ruce (rectangles místo čar)
    canvas.create_rectangle(20, 170, 100, 200, fill="red")
    canvas.create_rectangle(200, 170, 270, 200, fill="red")
    # Nohy (rectangles místo čar)
    canvas.create_rectangle(115, 300, 145, 400, fill="purple")
    canvas.create_rectangle(155, 300, 185, 400, fill="purple")
    okno.mainloop()

if __name__ == "__main__":
    robot()