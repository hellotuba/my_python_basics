# program ktery rozhodne ze strany abc splnuji trojuhelnikovou nerovnost

stanaa = float(input("Zadej stranu a: "))
staanab = float(input("Zadej stranu b: "))
stanac = float(input("Zadej stranu c: "))

while stanaa <= 0 or staanab <= 0 or stanac <= 0:
    print("Strany musi byt kladne")
    stanaa = float(input("Zadej stranu a: "))
    staanab = float(input("Zadej stranu b: "))
    stanac = float(input("Zadej stranu c: "))
    
if stanaa + staanab > stanac and stanaa + stanac > staanab and staanab + stanac > stanaa:
    print("Strany splnuji trojuhelnikovou nerovnost")
else:
    print("Strany nesplnuji trojuhelnikovou nerovnost")
