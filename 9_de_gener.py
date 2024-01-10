""""
def contar_as(lletra_a):
    a = ('a')
    b = [0]
    for i, e in enumerate(lletra_a):
        if e in ['a']:
            b[0] += 1
    for i, e in enumerate(b):
        print("La lletra a es repeteix {} vegades".format(b))

#PPrincipal
a = input("Introdueix una frase: ")
contar_as(a)
"""
""""
def contar_caracters(a,b):
    num=0
    for e in a:
        if e==b:
            num+=1
    print("En la frase '{}' hi ha {} caracters '{}'".format(a,num,b))


#PPrincipal
a = input("Introdueix una frase: ")
b = input("Assigna el caracter que vols comptar: ")
contar_caracters(a,b)
"""
""""
def contar_caracters(a,b,c):
    numb=0
    numc=0
    for e in a:
        if e==b:
            numb+=1
        if e==c:
            numc+=1
    print("En la frase '{}' hi ha {} caracters '{}' i {} caracters '{}'".format(a,numb,b,numc,c))


#PPrincipal
a = input("Introdueix una frase: ")
b = input("Assigna el primer caracter que vols comptar: ")
c = input("Assigna el segon caracter que vols comptar: ")
contar_caracters(a,b,c)
"""
'''''
def contar_vocals(a):
    b = ['a', 'e', 'i', 'o', 'u']
    vocals = 0
    for e in a:
        if e in b:
            vocals += 1
    print("En la frase hi ha {} vocals".format(vocals))

#PPrincipal
a = input("Introdueixi una frase a analitzar: ")
contar_vocals(a)
'''''
'''''
def contar_vocals(a):
    b = ['a', 'e', 'i', 'o', 'u']
    c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','v','w','x','y','z']
    vocals = 0
    lletres = 0
    cespecials = 0
    for e in a:
        if e in b:
            vocals += 1
        elif e in c:
            lletres +=1
        else:
            cespecials +=1
    print("En la frase hi ha {} vocals i {} consonants, i {} caracters especials.".format(vocals,lletres,cespecials))

#PPrincipal
a = input("Introdueixi una frase a analitzar: ")
contar_vocals(a)
'''
''''
def contar_inicials():
    n = []
    a = input("Introdueix una frase: ")
    l = a.split(" ")
    for e in l:
            n.append(e[0])
    print("La primera lletra de cada paraula es {}".format(n))

#PPrincipal
contar_inicials()
'''
''''
def contar_inicials():
    n = []
    a = input("Introdueix una frase: ")
    l = a.split(" ")
    for e in l:
            n.append(len(e))
    print("La longitud de les paraules de la frase es {}".format(n))

#PPrincipal
contar_inicials()
'''



