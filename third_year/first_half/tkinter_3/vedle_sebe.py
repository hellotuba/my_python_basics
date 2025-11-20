import tkinter 
root = tkinter.Tk()
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(40, 50, 150, 150, fill="blue")
canvas.create_rectangle(150, 50, 260, 150, fill="lightblue")
canvas.create_rectangle(260, 50, 370, 150, fill="darkblue")
root.mainloop()