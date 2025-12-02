from datetime import datetime, timedelta

def llegir_dades():
    hores_inici = {}
    entregues = []

    with open("temps_inici.csv", encoding="utf-8") as fitxer_inici:
        for fila in fitxer_inici:
            camps = fila.strip().split(";")
            if camps[0] == "nom":
                continue
            hores_inici[camps[0]] = camps[1]

    with open("entregues.csv") as fitxer_entregues:
        for fila in fitxer_entregues:
            camps = fila.strip().split(";")
            if camps[0] == "nom":
                continue
            entregues.append(camps)

    return hores_inici, entregues


def punts_finals():
    hores_inici, entregues = llegir_dades()
    millors_notes = {}

    for entrega in entregues:
        nom = entrega[0]
        tasca = entrega[1]
        nota = int(entrega[2])

        hora_i, minut_i = hores_inici[nom].split(":")
        temps_inici = datetime(2000, 1, 1, int(hora_i), int(minut_i))

        hora_f, minut_f = entrega[3].split(":")
        temps_entrega = datetime(2000, 1, 1, int(hora_f), int(minut_f))

        if temps_entrega - temps_inici > timedelta(hours=3):
            continue

        if nom not in millors_notes:
            millors_notes[nom] = {}

        if tasca not in millors_notes[nom] or nota > millors_notes[nom][tasca]:
            millors_notes[nom][tasca] = nota

    puntuacions_totals = {}
    for nom, tasques in millors_notes.items():
        puntuacions_totals[nom] = sum(tasques.values())

    return puntuacions_totals


print(punts_finals())
