def treure_paraules (base_dades: str):
    paraules = []
    with open (base_dades) as llista_paraules:
        for paraula in llista_paraules:
            paraules.append(paraula.strip())
    return paraules

def comparador (paraula_usuari: str, paraula2:str):
    if paraula_usuari == paraula2:
        return True
    if "*" in paraula_usuari:
        if paraula_usuari [0] == "*":
            if paraula2.endswith(paraula_usuari[1:]):
                return True
        else:
            if paraula2.startswith(paraula_usuari[:len(paraula_usuari) - 2]):
                return True
        return False
            
    if "." in paraula_usuari:
        if len(paraula_usuari) == len(paraula2):
            for i in range (len(paraula_usuari)):
                if paraula_usuari [i] == "." or paraula_usuari [i] == paraula2 [i]:
                    continue
                else:
                    return False
            return True
        else:
            return False
    return False

def cerca_paraules (paraula_usuari: str, base_dades: list):
    resultats = []
    for paraula in base_dades:
        if comparador (paraula_usuari, paraula):
            resultats.append(paraula)
    return resultats


llista_paraules = treure_paraules ("paraules.txt")
print(cerca_paraules("*vokes", llista_paraules))