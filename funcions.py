#def intercanvi(a,b):
   # return b,a
#x = 'a'
#y = 'b'
#print("El valor d'x és {} i el d'y és {}".format(x,y))
#x,y = intercanvi (x,y)
#print("Després de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))

def major(x,y):
    if x>y:
        return x
    else:
        return y

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))
z = major(x,y)
print("El major de {} i {} és {}".format(x,y,z))