def persona_mes_vella(persones: list):
    min_any = persones [0] [1]
    persona_vella = persones [0] [0]
    for tupla in persones:
        if tupla [1] < min_any:
            persona_vella = tupla [0]
            min_any = tupla [1]
    return persona_vella 
            
    
p1 = ("Adam", 1977)
p2 = ("El·lena", 1985)
p3 = ("Maria", 1953)
p4 = ("Ernest", 1997)
persones = [p1, p2, p3, p4]

print(persona_mes_vella(persones))