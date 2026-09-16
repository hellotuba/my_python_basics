import tkinter as tk

okno = tk.Tk()
okno.title("Calc")

display = tk.Entry(okno, width=20, font=("Arial", 20), justify="right")

display.grid(row=0, column=0, columnspan=4)

def klik(hodnota):
    if hodnota == "=":
        try:
            vysledek = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(vysledek))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif hodnota == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, hodnota)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(okno, text=text, width=5, height=2, font=("Arial", 20),
                       command=lambda t=text: klik(t))
    button.grid(row=row, column=col)

okno.mainloop()
