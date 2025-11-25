import tkinter
canvas = tkinter.Canvas(height=200, width=200)
canvas.pack()
canvas.create_rectangle(0, 0, 200, 200, fill="blue")
canvas.create_rectangle(5, 5, 195, 195, fill="white")
canvas.create_rectangle(10, 10, 190, 190, fill="blue")
canvas.create_text(100, 100, text='80', fill="white", font=("Arial", 100))
canvas.mainloop()