def es_palindrom(a):
    a = a.lower()
    return a == a[::-1]
    
b = input("Introdueix una paraula: ")

if es_palindrom(b):
    print("Aquesta paraula es un palíndrom")
else:
    print("Aquesta paraula no es un palíndrom")