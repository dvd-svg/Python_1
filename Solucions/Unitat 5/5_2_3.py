def imprimeix_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i % 3 == 0:
            print()
        for j in range(len(sudoku [i])):
            if j % 3 == 0:
                print (" ", end="")
            if sudoku [i] [j] == 0:
                print ("_ ", end="")
            else:
                print (f"{sudoku [i] [j]} ", end="")
        print()

def afegeix_numero(sudoku: list, num_fila: int, num_columna: int, numero: int):
    sudoku [num_fila] [num_columna] = numero


sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


imprimeix_sudoku(sudoku)
afegeix_numero(sudoku, 0, 0, 2)
afegeix_numero(sudoku, 1, 2, 7)
afegeix_numero(sudoku, 5, 7, 3)
print()
print("S'han afegit tres números:")
print()
imprimeix_sudoku(sudoku)