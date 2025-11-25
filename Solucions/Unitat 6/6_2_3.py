def llegir_dades (base_dades: str):
    dades_sortida = []
    with open (base_dades) as arxiu_dades:
        for fila in arxiu_dades:
            dades_fila = {}
            elements = fila.split(";")
            dades_fila ["nom"] = elements [0].strip()
            dades_fila ["problema"] = elements [1].strip()
            dades_fila ["resultat"] = int(elements [2].strip())
            dades_sortida.append(dades_fila)
    return dades_sortida

def operar (operacio: str):
    n1 = int(operacio [0])
    n2 = int(operacio [2])
    operador = operacio [1]
    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2


def filtra__solucions ():
    notes = llegir_dades ("solucions.csv")
    correcte = []
    incorrecte = []
    for alumne in notes:
        if operar (alumne["problema"]) == alumne["resultat"]:
            correcte.append(alumne)
        else:
            incorrecte.append(alumne)
    
    with open ("correcte.csv", "w") as arxiu_correcte:
        for alumne in correcte:
            arxiu_correcte.write(f"{alumne['nom']};{alumne['problema']};{alumne['resultat']}\n")
    
    with open ("incorrecte.csv", "w") as arxiu_correcte:
        for alumne in incorrecte:
            arxiu_correcte.write(f"{alumne['nom']};{alumne['problema']};{alumne['resultat']}\n")


filtra__solucions ()            