import tkinter as tk
import random

FLAG_WIDTH = 300
FLAG_HEIGHT = 200

def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

root = tk.Tk()
root.title("Sportovní vlajka")

canvas = tk.Canvas(root, width=FLAG_WIDTH, height=FLAG_HEIGHT, bg="white")
canvas.pack()

x = random.randint(50, FLAG_WIDTH - 50)
y = random.randint(50, FLAG_HEIGHT - 50)

color1 = random_color()
color2 = random_color()
color3 = random_color()
color4 = random_color()

canvas.create_rectangle(0, 0, x, y, fill=color1, outline="black") 
canvas.create_rectangle(x, 0, FLAG_WIDTH, y, fill=color2, outline="black")  
canvas.create_rectangle(0, y, x, FLAG_HEIGHT, fill=color3, outline="black")  
canvas.create_rectangle(x, y, FLAG_WIDTH, FLAG_HEIGHT, fill=color4, outline="black") 

root.mainloop()