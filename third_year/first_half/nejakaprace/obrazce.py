def trojuhelnik():
    print("   *   ")
    print("  ***  ")
    print(" ***** ")
    print("*******")

def obdelnik():
    print("#######")
    print("#     #")
    print("#######")

def noha():
    print("   |  ")
    print("   |  ")
    print(" __|__")

def stromecek():
    trojuhelnik()
    trojuhelnik()
    noha()

def stomecek2():
    trojuhelnik()
    obdelnik()
    noha()

def nevimcotoje():
    obdelnik()
    noha()
    obdelnik()

def stextom():
    print("toto je noha:")
    noha()
    print()
    print("toto je obdelnik:")
    obdelnik()
    print()
    print("toto je trojuhelnik:")
    trojuhelnik()

print()
print()
stromecek()
print()
print()
stomecek2()
print()
print()
nevimcotoje()
print()
print()
stextom()