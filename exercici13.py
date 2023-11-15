# Definir una funció gran() que, donats dos números, retorni el major.

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))


if x>y:
    print("El nombre més gran és {}".format(x))

elif x<y:
    print("El nombre més gran és {}".format(y))

else:
    print("Els dos nombres són iguals")