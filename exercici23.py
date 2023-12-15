#Definir una funció que utilitzi crear_punts()
#i dibuixi una imatge per la pantalla.

def crear_punts(lista): # Definir la funció
    for num in lista: # recorrer els elements de la llista
        print("." * num) #Produir el nombre de punts indicats a la llista

def dibuixar_imatge(imatge): #Definició
    for linia in imatge: #Recorrer les linies
        crear_punts(linia) #Crida la funció de crear els punts

imatge_a_dibujar = [
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]
] #Llista de valors que indiquen el nombre de punts que es dibuixaràn a cada linia

dibuixar_imatge(imatge_a_dibujar) # Crida la funció de dibuixar