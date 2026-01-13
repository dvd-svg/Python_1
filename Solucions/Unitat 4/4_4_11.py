def mes_curta (llista):
    longitud_min = len(llista [0])
    index = 0
    for i in range (len(llista)):
        if len(llista [i]) < longitud_min:
            longitud_min = len (llista [i])
            index = i
    return llista [index]



llista_entrada = ["first", "second", "fourth", "eleventh"]

resultat = mes_curta(llista_entrada)
print(resultat)

llista_entrada = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

resultat = mes_curta(llista_entrada)
print(resultat)