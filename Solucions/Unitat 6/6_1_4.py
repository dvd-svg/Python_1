def demanar_arxius ():
    arxiu1 = input ("Informació dels estudiants: ")
    arxiu2 = input ("Exercicis completats: ")
    return (arxiu1, arxiu2)

def treure_dades_noms (arxiu: str):
    noms = {}
    with open (arxiu) as nou_arxiu:
        for linia in nou_arxiu:
            parts = linia.split(";")
            if parts[0] == "id":
                continue
            noms [parts [0]] = f"{parts [1].strip()} {parts [2].strip()}"
    return (noms)

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
    for (dni, nom) in noms_.items():
        print (f"{nom} {sum(notes [dni])}")

noms = treure_dades_noms("6_1_4_1.csv")
notes = treure_dades_notes("6_1_4_2.csv")
imprimir_dades (noms, notes)