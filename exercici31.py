def nums_que_comencen_per(llista_noms):
    comptador = 0
    for nom in llista_noms:
        if nom.lower().startswith('a'):
            comptador += 1
    return comptador

llista = ["Arnold", "Albert", "Mac Allister", "Alex", "Cristiano"]
resultat = nums_que_comencen_per(llista)

print("Hi ha {} nombres que comencen per la lletra 'a' ".format(resultat))