def duplica_elements(numeros: list):
    nova_llista = []
    for i in range(len(numeros)):
        nova_llista.append(numeros [i] * 2)
    return nova_llista
        
numeros = [2, 4, 5, 3, 11, -4]
numeros_duplicats = duplica_elements(numeros)
print("original:", numeros)
print("duplicats:", numeros_duplicats)