# Pots emprar els seguents simbols per fer operacions de comparació: >  <  ==  >=  =<

a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
if a >= b:
    print ('{} és major o igual que {} '.format(a,b))
else:
    print ('{} no és major ni igal que {}'.format(a,b))