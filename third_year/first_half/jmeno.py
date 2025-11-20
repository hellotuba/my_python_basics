import tkinter 
root = tkinter.Tk()
canvas = tkinter.Canvas(width=400, height=200, bg='white')
canvas.pack()
# Jméno pomocí čar Jakub
# J
canvas.create_line(50, 10, 50, 90, fill='black', width=3)
canvas.create_line(50, 90, 30, 110, fill='black', width=3)
canvas.create_line(30, 110, 10, 100, fill='black', width=3)
# A
canvas.create_line(70, 110, 90, 10, fill='black', width=3)
canvas.create_line(90, 10, 110, 110, fill='black', width=3)
canvas.create_line(80, 60, 100, 60, fill='black', width=3)
# K
canvas.create_line(130, 10, 130, 110, fill='black', width=3)
canvas.create_line(130, 60, 170, 10, fill='black', width=3)
canvas.create_line(130, 60, 170, 110, fill='black', width=3)
# U
canvas.create_line(190, 10, 190, 90, fill='black', width=3)
canvas.create_line(190, 90, 230, 90, fill='black', width=3)
canvas.create_line(230, 90, 230, 10, fill='black', width=3)
# B
canvas.create_line(250, 10, 250, 110, fill='black', width=3)
canvas.create_line(250, 10, 295, 20, fill='black', width=3)
canvas.create_line(295, 20, 295, 45, fill='black', width=3)
canvas.create_line(295, 45, 250, 50, fill='black', width=3)
canvas.create_line(250, 50, 295, 60, fill='black', width=3)
canvas.create_line(295, 60, 295, 100, fill='black', width=3)
canvas.create_line(295, 100, 250, 110, fill='black', width=3)
canvas.create_text(200, 150, text='Jakub', font=('Arial', 30), fill='purple')
root.mainloop()