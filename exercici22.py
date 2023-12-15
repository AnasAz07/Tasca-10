def crear_punts(lista): #Definició de la funció
    for num in lista: #recorrer els elements de la llista
        print("." * num) #reproduir els punts

lista = input("Introduce los números separados por espacios: ") #Introduir la llista dels nombres de punts que es produiràn
numeros = [] #Passar els valors en una llista

for valor in lista.split(): #Recorrer els valors de la llista
    numeros.append(int(valor)) #Convertir els valors a numeros enters.

crear_punts(numeros) #Cridar la funció