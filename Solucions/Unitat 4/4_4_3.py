def llista_estels (llista):
    for fila in llista:
        for i in range(fila):
            print ("*", end="")
        print("")

llista_estels([3, 7, 1, 1, 2])