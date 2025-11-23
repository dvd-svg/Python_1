def histograma (cadena: str):
    lletres = {}
    
    for lletra in cadena:
        if lletra in lletres:
            lletres [lletra] += 1
        else:
            lletres [lletra] = 1
    
    for lletra in lletres:
        print (f"{lletra} ", end="")
        for i in range (lletres[lletra]):
            print("*", end="")
        print()

histograma("abba")
print()
histograma("estadísticament")
    
        