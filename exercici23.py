#Definir una funció que utilitzi crear_punts()
#i dibuixi una imatge per la pantalla.

def crear_punts(lista):
    for num in lista:
        print("." * num)

def dibuixar_imatge(imatge):
    for linia in imatge:
        crear_punts(linia)

imatge_a_dibujar = [
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]
]

dibuixar_imatge(imatge_a_dibujar)