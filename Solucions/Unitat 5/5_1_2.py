def comptar_elements_coincidents(matriu: list, element: int):
    coincidents = 0
    for fila in matriu:
        for num in fila:
            if num == element:
                coincidents += 1
    return coincidents

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(comptar_elements_coincidents(m, 1))