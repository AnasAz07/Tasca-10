def mostrar_majors_que(tupla, valor):
    for num in tupla:
        if num > valor:
            print(num)

tupla = input("Introdueix els numeros de la tupla separant per espais: ")
numeros = tuple(map(int, tupla.split()))
valor_limit = 18

print("Numeros majors que {}:".format(valor_limit))
mostrar_majors_que(numeros, valor_limit)
