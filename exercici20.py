def superposicio(x,y):  
    for element in x:
        if element in y:
            return True
    return False

x = input("Introdueix la primera llista: ")
y = input("Introdueix la segona llista: ")

if superposicio(x,y):
    print("Les llistes tenen elements en comú.")
else:
    print("No hi ha elements en comú.")

