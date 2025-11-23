def fila_correcta(sudoku: list, numero_fila: int):
    for casella in sudoku [numero_fila]:
        if casella != 0 and sudoku [numero_fila].count(casella) > 1:
                return False
    return True

def columna_correcta(sudoku: list, numero_columna: int):
    columna = []
    
    for fila in sudoku:
        columna.append(fila [numero_columna])
    
    for casella in columna:
        if casella != 0 and columna.count(casella) > 1:
            return False
    
    return True

def bloc_correcte(sudoku: list, numero_fila: int, numero_columna: int):
    numeros = []
    for i in range (numero_fila, numero_fila + 3):
        for j in range (numero_columna, numero_columna + 3):
            numeros.append (sudoku [i] [j])
    
    for numero in numeros:
        if numero != 0 and numeros.count(numero) > 1:
            return False
    
    return True

def graella_sudoku_correcta(sudoku: list):
    
    for i in range (len(sudoku)):
        if fila_correcta (sudoku, i) == False or columna_correcta (sudoku, i) == False:
            return False
    
    for i in range (0, 7, 3):
        for j in range (0, 7, 3):
            if bloc_correcte(sudoku, i, j) == False:
                return False
    
    return True


sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(graella_sudoku_correcta(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(graella_sudoku_correcta(sudoku2))