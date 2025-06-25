fullname = input("Zadejte svoje celé jméno: ")

parts = fullname.split()

initials = ''.join(part[0].upper() for part in parts)

print("Iniciály: ", initials)