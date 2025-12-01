import tkinter

def draw_japan_anime_uwu_flag():
    root=tkinter.Tk()
    canvas=tkinter.Canvas(width=600,height=400)
    canvas.pack()
    canvas.create_oval(200, 100, 400, 300, fill='red', outline='red')
    root.mainloop()

if __name__ == "__main__":
    draw_japan_anime_uwu_flag()