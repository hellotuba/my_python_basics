# mate 3 baliky obdelnikovych tvaru baliky se polozili na stul takze jsou za sebou sirka kazdeho je 100 a vyska je nahodne cislo od 10 do 200 vytvorte program ktery ho vykresli 3 barvami
import tkinter
import random
root = tkinter.Tk()
canvas = tkinter.Canvas(width=400, height=250)
canvas.pack()
cislicko = random.randint(10, 200)
cislicko2 = random.randint(10, 200)
cislicko3 = random.randint(10, 200)
back = f"#{random.randint(0, 0xFFFFFF):06x}"
back2 = f"#{random.randint(0, 0xFFFFFF):06x}"
back3 = f"#{random.randint(0, 0xFFFFFF):06x}"
canvas.create_rectangle(50, cislicko, 150, 240, fill=back)
canvas.create_rectangle(150, cislicko2, 250, 240, fill=back2)
canvas.create_rectangle(250, cislicko3, 350, 240, fill=back3)
root.mainloop()