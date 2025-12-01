import tkinter
root=tkinter.Tk()
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()
canvas.create_polygon(175,125, 325,125, 375,175, 375,325, 325,375, 175,375, 125,325, 125,175, fill="white", outline="black", width=6)
canvas.create_polygon(180,135, 320,135, 370,185, 370,315, 320,365, 180,365, 130,315, 130,185, fill="red", outline="red")
canvas.create_text(250,250, text="STOP", font=("Arial", 60, "bold"), fill="white")
root.mainloop()