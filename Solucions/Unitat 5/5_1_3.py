def qui_ha_guanyat(tauler_joc: list):
    cont1 = 0
    cont2 = 0
    for fila in tauler_joc:
        for casella in fila:
            if casella == 1:
                cont1 += 1
            elif casella == 2:
                cont2 += 1
    if cont1 > cont2:
        return 1
    if cont1 < cont2:
        return 2
    return 0

tauler1 = [[0, 1, 0],
           [0, 2, 1],
           [0, 1, 1]]


tauler2 = [[0, 1, 0, 0, 2],
           [2, 2, 0, 2, 0],
           [2, 1, 0, 2, 0],
           [2, 0, 0, 2, 2],
           [0, 1, 0, 1, 2]]

print (qui_ha_guanyat(tauler1))
print (qui_ha_guanyat(tauler2))