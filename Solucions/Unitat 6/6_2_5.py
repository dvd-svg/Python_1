def demanar_arxius ():
    arxiu1 = input ("Informació dels estudiants: ")
    arxiu2 = input ("Exercicis completats: ")
    arxiu3 = input ("Punts d'examen: ")
    arxiu4 = input ("Informació del curs: ")
    return (arxiu1, arxiu2, arxiu3, arxiu4)

def treure_dades_noms (arxiu: str):
    noms = {}
    with open (arxiu) as nou_arxiu:
        for linia in nou_arxiu:
            parts = linia.split(";")
            if parts[0] == "id":
                continue
            noms [parts [0]] = f"{parts [1].strip()} {parts [2].strip()}"
    return (noms)

def calcular_nota (exercicis: int, examen: int):
    suma = exercicis + examen
    
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
    notes_exercicis = {}
    notes_examen = {}
    notes_definitives = {}
    
    for dni, nom in noms_.items():
        notes_exercicis [dni] = (sum(exercicis_[dni]) * 10) // 40
        notes_examen [dni] = sum(examens_ [dni])
        
        notes_definitives [dni] = calcular_nota(notes_exercicis [dni], notes_examen [dni])
    
    return (notes_definitives)     

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

def treure_info_curs (arxiu: str):
    informacio = []
    with open (arxiu, encoding = "utf-8") as arxiu_curs:
        for fila in arxiu_curs:
            elements = fila.strip().split(":")
            informacio.append(elements[1].strip())
    return (f"{informacio [0]}, {informacio [1]} crèdits\n")

def imprimir_resultats (noms_: dict, exercicis_: dict, examen_: dict, info_curs_: str):
    notes = notes_finals(noms_, exercicis_, examen_)
    with open ("resultats.txt", "w") as arxiu_resultats:
        arxiu_resultats.write(info_curs_)
        subratllat = ""
        for i in range (len(info_curs_)):
            subratllat += "="
        arxiu_resultats.write(f"{subratllat}\n")
        arxiu_resultats.write (f"{'nom':30}{'num_ex':12}{'punts_ex':12}{'punts_exm':12}{'punts_tot':12}{'nota':12}\n")
        for dni, nom in noms_.items():
            num_ex = sum(exercicis_[dni])
            punts_ex = (num_ex * 10) // 40
            punts_exm = sum(examen_[dni])
            punts_tot = punts_ex + punts_exm
            nota = notes [dni]
            arxiu_resultats.write (f"{nom:30}{num_ex:<12}{punts_ex:<12}{punts_exm:<12}{punts_tot:<12}{nota:<12}\n")

def desar_resultats (noms_: dict, exercicis_: dict, examen_: dict):
    notes = notes_finals(noms_, exercicis_, examen_)
    with open ("resultats.csv", "w") as arxiu_resultats:
        for dni, nom in noms_.items():
            arxiu_resultats.write (f"{dni};{nom};{notes[dni]}\n")

noms = treure_dades_noms("6_1_4_1.csv")
exercicis = treure_dades_notes("6_1_4_2.csv")
examens = treure_dades_notes("6_1_5.csv")
info_curs = treure_info_curs("6_2_5.txt")

imprimir_resultats (noms, exercicis, examens, info_curs)
desar_resultats (noms, exercicis, examens)