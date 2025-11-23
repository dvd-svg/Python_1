def persones_mes_grans(persones: list, any_: int):
    persones_grans = []
    for persona in persones:
        if persona [1] < any_:
            persones_grans.append(persona[0])
    return persones_grans
    

p1 = ("Adam", 1977)
p2 = ("El·lena", 1985)
p3 = ("Maria", 1953)
p4 = ("Ernest", 1997)
persones = [p1, p2, p3, p4]

mes_grands = persones_mes_grans(persones, 1979)
print(mes_grands)