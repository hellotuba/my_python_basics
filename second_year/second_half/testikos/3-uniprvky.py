# 3. Napište program, který vrátí seznam obsahující každý prvek ze seznamu my_list právě jedenkrát (v pořadí prvních výskytů v původním seznamu).

my_list = [3, 7, 5, 3, 1, 2, 3, 1, 7]
print("Původní seznam:", my_list, "\n======================================")
uq_list = []
for item in my_list:
    if item not in uq_list:
        uq_list.append(item)
    else:
        print("Nalezen duplicitní prvek:", item)
print("\n======================================")
print("Seznam bez duplicit:", uq_list)