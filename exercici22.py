def crear_punts(lista):
    for num in lista:
        print("." * num)

lista = input("Introduce los números separados por espacios: ")
numeros = []

for valor in lista.split():
    numeros.append(int(valor))

crear_punts(numeros)