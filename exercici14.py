# Definir una funció gran_de_tres(), donats tres números, retorni el major.

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))
z = int(input("Introdueix el tercer nombre: "))

if x>y>z:
    print("El nombre més gran és {}".format(x))
elif x>z>y:
    print("El nombre més gran és {}".format(x))
elif x>y==z:
    print("El nombre més gran és {}".format(x))
elif z>x>y:
    print("El nombre més gran és {}".format(z))
elif x==z>y:
    print("El nombre més gran és {}".format(x))
elif y>x>z:
    print("El nombre més gran és {}".format(y))
elif y>z>x:
    print("El nombre més gran és {}".format(y))
elif y>x==z:
    print("El nombre més gran és {}".format(y))
elif z>y>x:
    print("El nombre més gran és {}".format(z))
elif y==z>x:
    print("El nombre més gran és {}".format(y))
elif x==y==z:
    print("Els tres nombres són iguals")
elif x==y>z:
    print("El nombre més gran és {}".format(x))