def invertir(diccionari: dict):
    claus = []
    valors = []

    for clau in diccionari:
        claus.append(clau)
        valors.append(diccionari[clau])
    
    diccionari.clear()
        
    for i in range (len(claus)):
        diccionari [valors [i]] = claus [i]
        
        
s = {1: "primer", 2: "segon", 3: "tercer", 4: "quart"}
invertir(s)
print(s)