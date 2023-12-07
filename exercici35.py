import random
import time

# Funció on expliquem què passa
def intro():
    print("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
    """)

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot, punts):
    print("T'estas apropant al talaiot...")
    time.sleep(2)
    print("Està fosc i és tenebrós...")
    time.sleep(2)
    print("Un gran gegant salta davant teu, t'agafa i ...")
    print("")
    time.sleep(2)
    gegantamic = random.randint(1, 2)
    if canviTalaiot == str(gegantamic):
        print("Et convida a menjar...")
        punts[0] += 1
        print("Has guanyat! Puntuació actual: {}".format(punts[0]))
    else:
        print("Se't menja d'un mos...ÑAMÑAMÑAM")

# Funció principal 
partidaNova = "si"
while partidaNova.lower() in ["s", "si"]:
    punts = [0]
    intro()
    nTalaiot = canviTalaiot()
    trobada(nTalaiot, punts)
    partidaNova = input("Vols tornar a menjar (jugar)? Introdueixi si o no: ")
    print("\n")

print("Has acumulat un total de {} punts. Gràcies per jugar!".format(punts[0]))
