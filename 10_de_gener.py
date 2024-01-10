''''
x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))

if x>y:
    print("La potencia del més petit {} pel més gros {} és {}".format(y,x,y**x))
elif y>x:
    print("La potencia del més petit {} pel més gros {} és {}".format(x,y,x**y))
else:
    print("La potencia del més petit {} pel més gros {} és {}".format(y,x,y**x))
  '''
''''
x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))

if y>0:
    print("El resulta de {} dividit entre {} dona {}".format(x,y,x/y))
else:
    print("Error, no es pot dividir un nombre per 0")
'''
''''
x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))

if y>0 and y<6 or y>9 and y<21:
    print("El resulta de {} dividit entre {} dona {}".format(x,y,x/y))
else:
    print("Error")
'''
'''''
x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))

if x>=5 and y<=5:
    print("El resulta de {} dividit entre {} dona {}".format(x,y,x/y))
elif x<5 and y<10:
    print("El resulta de {} dividit entre {} dona {}".format(y,x,y/x))
else:
    print("Error")
    '''
''''
x = input("introdueix una paraula: ")
b = len (x)
match b:
    case 1:
        print("La longitud de la paraula {} és de 1 caracter".format(x))
    case 2:
        print("La longitud de la paraula {} és de 2 caracters".format(x))
    case 3:
        print("La longitud de la paraula {} és de 3 caracters".format(x))
    case 4:
        print("La longitud de la paraula {} és de 4 caracters".format(x))
    case 5:
        print("La longitud de la paraula {} és de 5 caracters".format(x))
    case other:
        print("La longitud de la paraula {} és de més de 5 caracters".format(x))
'''
''''
x = int(input("Introdueix la teva edat: "))
if x>=0 and x<=7:
    print("Estas despertant el chakra 1")
elif x>=7 and x<=14:
    print("Estas despertant el chakra 2")
elif x>=14 and x<=21:
    print("Estas despertant el chakra 3")
elif x>=21 and x<=28:
    print("Estas despertant el chakra 4")
elif x>=28 and x<=35:
    print("Estas despertant el chakra 5")
elif x>=35 and x<=42:
    print("Estas despertant el chakra 6")
elif x>=42 and x<=49:
    print("Estas despertant el chakra 7")
else:
    print("Ja has despertat tots els chakres")
'''
''''
def llegir_llista():
    a = []
    c = "1"
    while c != ".":
        c = (input("Introdueixi un element de la llista i punt (.) per acabar: "))
        if c != ".":
            a.append(int(c))
        else:
            return a

def filtrar_edats(l):
    v = []
    s = []
    for e in l:
        if e >= 18:
            v.append(e)
        else:
            s.append(e)
    print("Els majors d'edat son {} i els menors son {}".format(v,s))
    
    

#PPrincipal
a = llegir_llista()
filtrar_edats(a)
'''
def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = (input("Introdueixi un element de la llista i punt (.) per acabar: "))
        if c != ".":
            a.append((c))
        else:
            return a
        
def filtrar_inicials_vocals_consonants(l):
    v = []
    s = []
    for e in l:
        if e[0] in ['a','e','i','o','u']:
            v.append(e)
        elif e[0] in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']:
            s.append(e)
    print("Les paraules que comencen per vocals son {} i les que comencen per consonants son {}".format(v,s))

#PPrincipal
a = llegir_llista()
filtrar_inicials_vocals_consonants(a)