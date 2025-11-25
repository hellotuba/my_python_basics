import tkinter
canvas = tkinter.Canvas(height=400, width=300)
canvas.pack()
canvas.create_rectangle(0, 0, 300, 400, fill="blue")
canvas.create_rectangle(5, 5, 295, 395, fill="white")
canvas.create_rectangle(10, 10, 290, 390, fill="blue")
canvas.create_text(150, 200, text='P', fill="white", font=("Arial", 150))
canvas.mainloop()