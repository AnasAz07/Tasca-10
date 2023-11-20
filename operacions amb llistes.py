# Pots fer cualsevol operació (+  -  *  /)

def llegir_llista():
    a = '1'
    l = []
    while a!='a':
        a=input("Introdueix un numero diferent a 'a': ")
        if a !='a':
            l.append(int(a))
        else:
            return l

# Programa Principal
a = llegir_llista()
b = llegir_llista()
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
print("La operació de la llista {} * {} és {}".format(a,b,c))
