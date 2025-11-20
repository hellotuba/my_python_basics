import tkinter as tk
import tkinter.messagebox as messagebox
import webbrowser as web
url = "https://hellotuba.eu/"
msgtext = "your computer is coocked"
root = tk.Tk()
root.title("NecoInter")
canvas = tk.Canvas(root)
canvas.create_rectangle(40, 20, 140, 110, fill="blue")
canvas.create_rectangle(210, 20, 310, 110, fill="red")
canvas.create_rectangle(40, 150, 140, 240, fill="green")
canvas.create_rectangle(210, 150, 310, 240, fill="yellow")
tk.Button(root, text="Click on me for suprise!", command=lambda: web.open(url) and messagebox.showinfo("Surprise!", msgtext)).pack()
canvas.pack()
root.mainloop()