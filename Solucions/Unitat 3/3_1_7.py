limit = int(input("Límit superior: "))
numero = 2
suma = 1
operacio = "1"

while suma <= limit:
    suma += numero
    operacio += f" + {numero}"
    numero += 1
    
print (f"La suma consecutiva: {operacio} = {suma}")
