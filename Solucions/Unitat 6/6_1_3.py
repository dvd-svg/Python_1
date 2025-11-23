def suma_matriu (base_dades: list):
    suma = 0
    for fila in base_dades:
        for valor in fila:
            suma += valor
    return suma

def maxim_matriu (base_dades: list):
    maxim = base_dades [0] [0]
    for fila in base_dades:
        for valor in fila:
            if valor > maxim:
                maxim = valor
    return maxim

def sumes_files (base_dades: list):
    sumes = []
    for fila in base_dades:
        sumes.append (sum(fila))
    return sumes
    

    
def generar_matriu (arxiu: str):
    matriu = []
    with open (arxiu) as nou_arxiu:
        for linia in nou_arxiu:
            linia = linia.replace("\n", "")
            linia = linia.split(",")
            for i in range(len(linia)):
                linia [i] = int(linia [i])
            matriu.append(linia)
    return matriu

def imprimir_matriu (base_dades: list):
    for fila in base_dades:
        for valor in fila:
            print (f"{valor} ", end = "")
        print()

matriu = generar_matriu ("matriu.txt")
imprimir_matriu (matriu)
print (f"suma matriu: {suma_matriu (matriu)}")
print (f"màxim matriu: {maxim_matriu (matriu)}")
print (f"sumes files: {sumes_files (matriu)}")