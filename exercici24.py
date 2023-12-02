def gran_llista(lista):
    return max(lista, default=None)

input_lista = input("Introduce la lista de números separados por espacios: ")

numeros = [int(x) for x in input_lista.split()]

resultado = gran_llista(numeros)

if resultado is not None:
    print("El número más grande es {}".format(resultado))
else:
    print("La lista está vacía")