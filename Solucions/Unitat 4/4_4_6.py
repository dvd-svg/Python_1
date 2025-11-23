def suma_positius (llista):
    suma = 0
    for num in llista:
        if num > 0:
            suma += num
    return suma

llista_entrada = [1, -2, 3, -4, 5]
resultat = suma_positius(llista_entrada)
print("El resultat és", resultat)