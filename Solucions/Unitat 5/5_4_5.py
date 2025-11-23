def crear_quadrat (llista: list, n_capes: int):
    costat = ((n_capes - 1 )* 2) + 1
    for i in range (costat):
        llista.append([])
        for j in range (costat):
            llista [i].append ("0")
            
def imprimir_quadrat (llista: list):
    for fila in llista:
        for valor in fila:
            print (valor, end="")
        print()

def iterar (tupla: tuple):
    return (tupla [0] + 1, tupla [1] - 1)

def omplir_quadrat (llista: list):
    lletres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    limits = 0 , len(llista)
    
    for i in range (int (((len(llista) - 1) / 2) + 1), 0, -1):
        for j in range (limits [0], limits [1]):
            for k in range (limits [0], limits [1]):
                llista [j] [k] = lletres [i - 1]
        limits = iterar(limits)

def main():
    capes = int(input("Capes: "))
    print ()
    print ()
    quadrat = []
    crear_quadrat (quadrat, capes)
    omplir_quadrat(quadrat)
    imprimir_quadrat(quadrat) 
    
main()



