def linia (cops, cadena):
    if cadena == "":
        cadena = "*"
    print (cadena [0] * cops)

def quadrat (mida, caracter):
    i = 0
    while i < mida:
        linia (mida, caracter)
        i += 1

quadrat(5, "*")
print()
quadrat(3, "o")