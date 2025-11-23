def longitud_mes_llarga (llista):
    longitud_max = 0
    for paraula in llista:
        if len(paraula) > longitud_max:
            longitud_max = len (paraula)
    return longitud_max



llista_entrada = ["first", "second", "fourth", "eleventh"]

resultat = longitud_mes_llarga(llista_entrada)
print(resultat)

llista_entrada = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

resultat = longitud_mes_llarga(llista_entrada)
print(resultat)