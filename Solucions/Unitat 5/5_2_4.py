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

def copia_i_afegeix(sudoku: list, num_fila: int, num_columna: int, numero: int):
    nou_sudoku = []
    
    for i in range (len(sudoku)):
        nou_sudoku.append ([])
        for j in range (len (sudoku [i])):
            nou_sudoku [i].append(sudoku [i] [j])
            
    nou_sudoku [num_fila] [num_columna] = numero
    
    return nou_sudoku

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

copia_graella = copia_i_afegeix(sudoku, 0, 0, 2)
print("Original:")
imprimeix_sudoku(sudoku)
print()
print("Còpia:")
imprimeix_sudoku(copia_graella)