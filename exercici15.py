# Definir una funció que calculi la longitud d’una llista o d’una cadena donada.

def contar_caràcters(element):
    return len(str(element))

a = input("Introdueix una llista o cadena de caràcters: ")
b = contar_caràcters(a)

print("La llista o cadena de caràcters té {} caràcters".format(b))



