# Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas 
# contrari retorni fals.

def detectar_vocals(a):
    l = ('a', 'e', 'i', 'o', 'u')
    d = a.lower()
    if d in l:
        print("És Vocal")
    else:
        print("No és vocal")

a = input("Introdueix un caràcter: ")
b = detectar_vocals(a)