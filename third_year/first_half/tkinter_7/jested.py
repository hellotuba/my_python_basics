# vytovorit pomoci obdelniku na tkniter vysílač Ještěd. Kreslení začneš od spodního obdélníku. Ten má šířku 210 a výšku 10. Každý další obdélník leží na předchozím, je užší o 40 a vyšší o 10
import tkinter

def jested(platno, x, y):
    sirka = 210
    vyska = 10
    for i in range(6):
        offset = (210 - sirka) / 2
        platno.create_rectangle(x + offset, y - vyska, x + offset + sirka, y, fill="gray", outline="black")
        y -= vyska
        sirka -= 40

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Ještěd")
    platno = tkinter.Canvas(root, width=300, height=300, bg="white")
    platno.pack()
    jested(platno, 50, 250)
    root.mainloop()