def deu_vegades(index_inici: int, index_fi: int):
    diccionari = {}
    for i in range(index_inici, index_fi + 1):
        diccionari [i] = i * 10
    return diccionari

d = deu_vegades(3, 6)
print(d)