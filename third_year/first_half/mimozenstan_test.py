# Napis program mimozemstan, ktery pomoci barevnych obdelniku vytvori obrazek hlavu mimozemstana na hlave by meli byt 2 stejne oci a jedna usta souradnice hlavy jsou ulozeny v promenych X Y.
# bude fungovat spravne kdyz hodnotu x zvetsite o 30 a hodnotu y zvetsite o 40?
zadaniX = int(input("\nZadej hodnotu X: "))
zadaniY = int(input("\nZadej hodnotu Y: "))
kolikpridat = int(input("\nO kolik zvetsit souradnice X a Y (pokud nezvětsovat zadejte 0): "))
if kolikpridat < 0:
    print("\nZadejte kladnou hodnotu nebo 0.\n")
    kolikpridat = int(input("\nO kolik zvetsit souradnice X a Y (pokud nezvětsovat zadejte 0): "))
import tkinter
root = tkinter.Tk()
root.title("Mimozemstan")
canvas = tkinter.Canvas(root, width=650, height=650)
canvas.pack()
X = zadaniX + kolikpridat
Y = zadaniY + kolikpridat
# hlava
canvas.create_rectangle(X-50, Y-50, X+50, Y+50, fill="lime")
# oci
canvas.create_rectangle(X-30, Y-20, X-10, Y+10, fill="white") 
canvas.create_rectangle(X+10, Y-20, X+30, Y+10, fill="white")
canvas.create_rectangle(X-20, Y-10, X-15, Y+5, fill="black")  
canvas.create_rectangle(X+15, Y-10, X+20, Y+5, fill="black")  
# usta
canvas.create_rectangle(X-20, Y+20, X+20, Y+30, fill="red")
root.mainloop()