def tot_invertit (llista):
    llista_invertida = []
    for i in range (len(llista) -1, -1, -1):
        llista_invertida.append(llista [i] [::-1])
    return llista_invertida


llista_paraules = ["Hola", "allà", "exemple", "un més"]
nova_llista = tot_invertit(llista_paraules)
print(nova_llista)