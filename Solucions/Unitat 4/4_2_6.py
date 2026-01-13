def linia (cops, cadena):
    if cadena == "":
        cadena = "*"
    print (cadena [0] * cops)

def figura (triangle, caracter_triangle, rectangle, caracter_rectangle):
    i = 1
    while i <= triangle:
        linia (i, caracter_triangle)
        i += 1
    i = 0
    while i < rectangle:
        linia (triangle, caracter_rectangle)
        i+= 1
    

figura(5, "X", 3, "*")
print()
figura(2, "o", 4, "+")
print()
figura(3, ".", 0, ",")