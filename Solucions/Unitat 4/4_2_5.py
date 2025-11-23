def linia (cops, cadena):
    if cadena == "":
        cadena = "*"
    print (cadena [0] * cops)

def triangle (mida):
    i = 1
    while i <= mida:
        linia (i, "#")
        i += 1

triangle(6)
print()
triangle(3)