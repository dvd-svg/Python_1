def suma_llistes (llista1, llista2):
    suma = []
    for i in range (len(llista1)):
        suma.append(llista1 [i] + llista2 [i])
    return suma

a = [1, 2, 3]
b = [7, 8, 9]
print(suma_llistes(a, b))
        