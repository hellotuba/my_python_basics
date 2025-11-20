import tkinter
def kriz():
    okno = tkinter.Tk()
    okno.title("Červený kříž")
    okno.geometry("300x300")
    canvas = tkinter.Canvas(okno, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_rectangle(25, 125, 225, 175, fill="red")
    canvas.create_rectangle(100, 50, 150, 250, fill="red")
    okno.mainloop()

if __name__ == "__main__":
    kriz()
