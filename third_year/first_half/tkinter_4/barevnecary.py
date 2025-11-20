import tkinter
root = tkinter.Tk()
root.title("Barevne cary")
canvas = tkinter.Canvas(root, width=650, height=650, background="#FDFDFD")
canvas.pack()
# modre carky
canvas.create_line(50, 50, 450, 450, fill="blue", width=5)
canvas.create_line(65, 50, 450, 435, fill="blue", width=5)
canvas.create_line(85, 50, 450, 415, fill="blue", width=5)
canvas.create_line(100, 50, 450, 400, fill="blue", width=5)
# zluta carky
canvas.create_line(55, 50, 450, 445, fill="yellow", width=5)
canvas.create_line(95, 50, 450, 405, fill="yellow", width=5)
# zelene carky
canvas.create_line(60, 50, 450, 440, fill="green", width=5)
canvas.create_line(90, 50, 450, 410, fill="green", width=5)
# cerne carky
canvas.create_line(75, 50, 450, 425, fill="black", width=5)
root.mainloop()