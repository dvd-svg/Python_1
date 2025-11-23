def nombres_parells (llista):
    parells = []
    for num in llista:
        if num % 2 == 0:
            parells.append(num)
    return parells

llista_entrada = [1, 2, 3, 4, 5]
nova_llista = nombres_parells(llista_entrada)
print("original", llista_entrada)
print("nova", nova_llista)