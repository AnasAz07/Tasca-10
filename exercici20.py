def superposicio(x,y):  # Definició de la funció
    for element in x: # Recorrer els elements de les llistes
        if element in y: #Si hi ha un element en comú entre x i y:
            return True 
    return False

x = input("Introdueix la primera llista: ") #Introduir les llistes 
y = input("Introdueix la segona llista: ")

if superposicio(x,y): #Cridar la funció
    print("Les llistes tenen elements en comú.")
else:
    print("No hi ha elements en comú.")

