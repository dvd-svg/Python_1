from datetime import datetime, timedelta

def treure_dades ():
    dades_inici = {}
    dades_entregues = []

    with open ("temps_inici.csv", encoding = "utf-8") as arxiu_inici:
        for fila in arxiu_inici:
            valors = fila.strip().split(";")
            if valors [0] == "nom":
                continue
            dades_inici [valors[0]] = valors [1]
            
    with open ("entregues.csv") as arxiu_entregues:
        for fila in arxiu_entregues:
            valors = fila.strip().split(";")
            if valors [0] == "nom":
                continue
            dades_entregues.append(valors)
            
    return (dades_inici, dades_entregues)

def eliminar_duplicats (llista: list):
    llista_definitiva = []
    
    for item in llista:
        if not (item in llista_definitiva):
            llista_definitiva.append(item)
    
    return llista_definitiva

def tramposos ():
    dades = treure_dades ()
    dades_inici = dades [0]
    dades_entregues = dades [1]
    
    llista_tramposos = []

    for entrega in dades_entregues:
        hora_inici = int (dades_inici [entrega [0]].split (":") [0])
        minut_inici = int (dades_inici [entrega [0]].split (":") [1])
        hora_ex = int(entrega [3].split(":") [0])
        minut_ex = int(entrega [3].split(":") [1])
        
        data_inici = datetime (2000, 1, 1, hora_inici, minut_inici)
        data_ex = datetime (2000, 1, 1, hora_ex, minut_ex)
        diferencia = data_ex - data_inici
        if (diferencia > timedelta (hours = 3)):
            llista_tramposos.append (entrega [0])
    
    return eliminar_duplicats (llista_tramposos)   
        

print (tramposos())
