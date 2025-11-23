def llegir_fruites (arxiu: str):
    diccionari = {}
    with open (arxiu) as nou_arxiu:
        for linia in nou_arxiu:
            parts = linia.split(";")
            (fruita, preu) = (parts [0], parts[1])
            diccionari [fruita] = float(preu)
    return diccionari

print (llegir_fruites ("fruites.csv"))