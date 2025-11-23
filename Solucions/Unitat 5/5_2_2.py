def elimina_menor(numeros: list):
    numeros.remove(min(numeros))
    
numeros = [2, 4, 6, 1, 3, 5]
elimina_menor(numeros)
print(numeros)