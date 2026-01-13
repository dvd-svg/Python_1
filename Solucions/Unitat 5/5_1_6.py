def bloc_correcte(sudoku: list, numero_fila: int, numero_columna: int):
    numeros = []
    for i in range (numero_fila, numero_fila + 3):
        for j in range (numero_columna, numero_columna + 3):
            numeros.append (sudoku [i] [j])
    
    for numero in numeros:
        if numero != 0 and numeros.count(numero) > 1:
            return False
    
    return True
    
sudoku = [
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

print(bloc_correcte(sudoku, 0, 0))
print(bloc_correcte(sudoku, 1, 2))
            

        