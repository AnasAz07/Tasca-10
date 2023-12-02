def invertir(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

cadena_original = input("Introdueix una cadena de caràcters: ")

cadena_invertida = invertir(cadena_original)

print("La cadena invertida sería així: {}".format(cadena_invertida))