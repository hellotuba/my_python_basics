import tkinter

def scitani():
    vysledek.config(text=float(entry1.get()) + float(entry2.get()))

def odcitani():
    vysledek.config(text=float(entry1.get()) - float(entry2.get()))

def nasobeni():
    vysledek.config(text=float(entry1.get()) * float(entry2.get()))

def deleni():
    vysledek.config(text=float(entry1.get()) / float(entry2.get()))

root = tkinter.Tk()
root.title("Kalkulačka")

entry1 = tkinter.Entry(root)
entry1.pack()
entry2 = tkinter.Entry(root)
entry2.pack()

tkinter.Button(root, text="+", command=scitani).pack()
tkinter.Button(root, text="-", command=odcitani).pack()
tkinter.Button(root, text="*", command=nasobeni).pack()
tkinter.Button(root, text="/", command=deleni).pack()

vysledek = tkinter.Label(root, text="")
vysledek.pack()

root.mainloop()