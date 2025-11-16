nombre = int(input("Escriu un nombre: "))

operador1 = 1
operador2 = 1

while operador1 <= nombre:
    operador2 = 1
    while operador2 <= nombre:
        print (operador1, "x", operador2, "=", operador1 * operador2)
        operador2 += 1
    operador1 += 1

    