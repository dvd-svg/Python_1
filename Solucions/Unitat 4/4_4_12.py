def totes_les_llargues (llista):
    longitud_max = 0
    llista_llargues = []
    for paraula in llista:
        if len(paraula) > longitud_max:
            longitud_max = len(paraula)
    for paraula in llista:
        if len(paraula) == longitud_max:
            llista_llargues.append(paraula)
    return llista_llargues



llista_entrada = ["first", "second", "fourth", "eleventh"]

resultat = totes_les_llargues(llista_entrada)
print(resultat)

llista_entrada = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

resultat = totes_les_llargues(llista_entrada)
print(resultat)