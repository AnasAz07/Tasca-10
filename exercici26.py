def filtrar_paraules(lista_paraules, x):
    for paraula in lista_paraules:
        if len(paraula) > x:
            print(paraula)

a = input("Introdueix les paraules separades per espais: ")

paraules = a.split()

x = int(input("Introdueix el nombre mínim de caràcters: "))

print("Paraules amb més de {} caràcters:".format(x))

filtrar_paraules(paraules, x)