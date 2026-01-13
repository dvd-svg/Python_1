def factorials(n: int):
    diccionari = {}
    for i in range (1, n +1):
        factorial = 1
        for j in range (1, i + 1):
            factorial *= j
        diccionari [i] = factorial
    return diccionari

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])