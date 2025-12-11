# jenom na platne nechate zobrazit 2 mocniny cisla v nemz budou cisla a jejich druhe mocniny 
import tkinter

def zobraz_mocninu(platno, cislo, exponent, x, y):
    mocnina = cislo ** exponent
    text = f"{cislo}^{exponent} = {mocnina}"
    platno.create_text(x, y, text=text, font=("Arial", 16), fill="black")

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Zobrazeni mocnin")
    platno = tkinter.Canvas(root, width=400, height=240, bg="white")
    platno.pack()
    for i in range(0, 11):
        zobraz_mocninu(platno, i, 2, 100, 20 + i * 20)
    root.mainloop()