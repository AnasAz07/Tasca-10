def canvi(l):
    x = int(input("Introdueix la clau a modificar o a afegir: "))
    l[x] = input("Introdueix el nou valor a aquesta clau: ")

# Programa Principal
a = {'a':3, 'b':5, 'c':7, 'd':9, 'e':10}
print("El valor del diccionari abans de canviar és: {}".format(a))
canvi(a)
print("El valor del diccionari després de canviar és: {}".format(a))


"""""
def canvi(l):
    x = input("Introdueix el valor a inserir: ")
    l.add(x)

# Programa Principal
a = {3, 5, 7, 9, 10}
print("El valor del conjunt abans de canviar és: {}".format(a))
canvi(a)
print("El valor del conjunt després de canviar és: {}".format(a))
"""
""""
def intercanvi(a,b):
   # return b,a
x = 'a'
y = 'b'
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y = intercanvi (x,y)
print("Després de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))
"""

""""
def major(x,y):
    if x>y:
        return x
    else:
        return y

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))
z = major(x,y)
print("El major de {} i {} és {}".format(x,y,z))
"""
""""
def canvi(l):
    x = int(input("Introdueix la posició a modificar: "))
    l[x] = input("Introdueix el valor a inserir: ")

# Programa Principal
a = [3, 4, 5, 6, 7, 8, 'a', (1,2), (3,4), 10]
print("El valor de la llista abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la llista després de canviar és: {}".format(a))
"""