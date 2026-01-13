import math


def obtenir_dades_estacions(fitxer: str):
    coordenades = {}
    with open (fitxer) as nou_arxiu:
        for fila in nou_arxiu:
            valors = fila.split(";")
            if valors[0] == "Longitud":
                continue
            coordenades [valors[3].strip()] = (float(valors [0].strip()), float(valors [1].strip()))
    return coordenades


def distancia(estacions_: dict, estacio1: str, estacio2: str):
    x_km = (estacions_ [estacio1] [0] - estacions_ [estacio2] [0]) * 83.4
    y_km = (estacions_ [estacio1] [1] - estacions_ [estacio2] [1]) * 111.2
    distancia_km = math.sqrt(x_km**2 + y_km**2)
    return distancia_km


def distancia_mes_gran(estacions_: dict):
    max_distancia = ("", "", 0)
    for estacio1 in estacions_:
        for estacio2 in estacions_:
            if estacio1 == estacio2:
                continue
            distancia_ = distancia(estacions_, estacio1, estacio2)
            if distancia_ > max_distancia [2]:
                max_distancia = (estacio1, estacio2, distancia_)
    return max_distancia


estacions = obtenir_dades_estacions('estacions.csv')
estacio1, estacio2, mes_gran = distancia_mes_gran(estacions)
print(estacio1, estacio2, mes_gran)