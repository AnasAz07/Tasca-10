def crear_repetits(numero,caracter):
    return caracter * numero

numero = int(input("Introdueix un numero: "))
caracter = input("Introdueix un caràcter: ")

resultat = crear_repetits(numero,caracter)
print("Posant el caràcter {} multiplicat per {} dona {}".format(caracter,numero,resultat))
