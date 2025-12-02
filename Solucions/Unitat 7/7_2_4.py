from random import choice

dauA = [3, 3, 3, 3, 3, 6]
dauB = [2, 2, 2, 5, 5, 5]
dauC = [1, 4, 4, 4, 4, 4]

def tirar (dau: str):
    if dau == "A":
        resultat = choice(dauA)
    elif dau == "B":
        resultat = choice(dauB)
    elif  dau == "C":
        resultat = choice(dauC)
    else:
        raise ValueError(f"El dau seleccionat: {dau}\n no és una opció valida, selecciona A, B o C")
    return resultat

def jugar(dau1: str, dau2: str, cops: int):
    victories_dau1 = 0
    victories_dau2 = 0
    empats = 0

    for i in range (cops):
        resultat_dau1 = tirar (dau1)
        resultat_dau2 = tirar (dau2)
        if resultat_dau1 > resultat_dau2:
            victories_dau1 += 1
        elif resultat_dau1 < resultat_dau2:
            victories_dau2 += 1
        else:
            empats += 1
            
    return (victories_dau1, victories_dau2, empats)

resultat = jugar("A", "C", 1000)
print(resultat)
resultat = jugar("B", "B", 1000)
print(resultat)