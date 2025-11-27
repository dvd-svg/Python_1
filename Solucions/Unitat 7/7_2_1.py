from random import randint

def nombres_loteria (nombre: int, minim: int, maxim: int):
    llista_final = []
    
    if nombre > (maxim - minim + 1):
        raise ValueError ("El nombre de numeros de loteria no pot ser superior al rang de valors possibles")
    
    while len(llista_final) < nombre:
        n_aleatori = randint (minim, maxim)
        if n_aleatori in llista_final:
            continue
        llista_final.append(n_aleatori)
    
    return llista_final
        
for number in nombres_loteria (7, 1, 40):
    print(number)

