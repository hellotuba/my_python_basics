#
import tkinter
canvas=tkinter.Canvas(height=400, width=400)
canvas.pack()
#okraje
canvas.create_text(40, 200, text='Levý okraj')
canvas.create_text(200, 10, text='Horní okraj')
canvas.create_text(360, 200, text='Pravý okraj')
canvas.create_text(200, 390, text='Dolní okraj')
#ctverec
canvas.create_rectangle(100, 100, 300, 300)
canvas.create_text(95, 95, text='A')
canvas.create_text(305, 95, text='B')
canvas.create_text(95, 305, text='C')
canvas.create_text(305, 305, text='D')
canvas.mainloop()