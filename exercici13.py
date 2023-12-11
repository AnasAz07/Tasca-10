# Definir una funció gran() que, donats dos números, retorni el major.
def gran(x,y):
    if x>y:
        print("El nombre més gran és {}".format(x))

    elif x<y:
        print("El nombre més gran és {}".format(y))

    else:
        print("Els dos nombres són iguals")

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))

gran(x,y)