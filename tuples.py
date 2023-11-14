def tercera_ocurrencia(l,e):
    a = l.count(e)
    if a==0:
        print("No hi ha ocurrències d'aquest element")
    elif a==1:
        print("La primera ocurrència de l'element està en la posició {}".format(l.index(e)))
    elif a>2:
        print("Hi ha més de dues ocurrències de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index(e,(so+1))
        print(to)
    else:
        print("Només hi ha zero o una ocurrència")

#Programa Principal
l=(1, 4, 2, (1, 3, 3), 4, 2, 1, 3, 4, 6, 1, 8)
x = int(input("Elegeix l'element que vol cercar la tercera ocurrencia: "))
tercera_ocurrencia(l,x)
