numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
operacio = input("Operació:")

if operacio == "sumar":
    print (f"{numero1} + {numero2} = {numero1 + numero2}")
    if operacio == "restar":
        print (f"{numero1} - {numero2} = {numero1 - numero2}")
        if operacio == "multiplicar":
            print (f"{numero1}  {numero2} = {numero1 * numero2}")