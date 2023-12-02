def superposicio(x,y):  
    for element in x:
        if element in y:
            return True
    return False

x = input("Introdueix la primera llista separant cada caràcter per espais: ")
y = input("Introdueix la segona llista separant cada caràcter per espais: ")

if superposicio(x,y):
    print("Les llistes tenen elements en comú.")
else:
    print("No hi ha elements en comú.")

