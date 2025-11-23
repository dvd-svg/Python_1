def demanar_arxius ():
    arxiu1 = input ("Informació dels estudiants: ")
    arxiu2 = input ("Exercicis completats: ")
    arxiu3 = input ("Punts d'examen: ")
    return (arxiu1, arxiu2, arxiu3)

def treure_dades_noms (arxiu: str):
    noms = {}
    with open (arxiu) as nou_arxiu:
        for linia in nou_arxiu:
            parts = linia.split(";")
            if parts[0] == "id":
                continue
            noms [parts [0]] = f"{parts [1].strip()} {parts [2].strip()}"
    return (noms)

def calcular_nota (exercicis: list, examen: list):
    nota_exercicis = (sum(exercicis) * 10) // 40
    nota_examen = sum(examen)
    
    suma = nota_exercicis + nota_examen
    
    if 0 <= suma < 15:
        return 0
    if 15 <= suma < 18:
        return 1
    if 18 <= suma < 21:
        return 2
    if 21 <= suma < 24:
        return 3
    if 24 <= suma < 28:
        return 4
    if 28 <= suma:
        return 5    

def notes_finals (noms_: dict, exercicis_: dict, examens_: dict):
    notes = {}
    for dni, nom in noms_.items():
        notes [dni] = calcular_nota(exercicis_ [dni], examens_ [dni])
    return notes     

def treure_dades_notes (arxiu: str):
    notes = {}
    with open (arxiu) as nou_arxiu:
        for linia in nou_arxiu:
            parts = linia.split(";")
            if parts[0] == "id":
                continue
            notes_alumne = []
            for i in range(1, len(parts)):
                notes_alumne.append(int(parts[i]))
            notes [parts [0]] = notes_alumne
    return (notes)

def imprimir_dades (noms_: dict, notes_: dict):
    for dni, nom in noms_.items():
        print (f"{nom} {notes [dni]}")


noms = treure_dades_noms("6_1_4_1.csv")
exercicis = treure_dades_notes("6_1_4_2.csv")
examens = treure_dades_notes("6_1_5.csv")

notes = notes_finals(noms, exercicis, examens)

imprimir_dades (noms, notes)


