def serie_mes_llarga_veins (llista):
    max_veins = 0
    veins = 1
    for i in range (len(llista) - 2):
        if llista [i] + 1 == llista [i + 1] or llista [i] - 1 == llista [i + 1]:
            veins += 1
            if veins > max_veins:
                max_veins = veins
        else:
            veins = 1
    return max_veins
        
        



llista_nombres = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(serie_mes_llarga_veins(llista_nombres))