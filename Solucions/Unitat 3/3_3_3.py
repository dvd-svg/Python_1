while True:
    nombre = int(input("Escriu un nombre: "))
    if nombre <= 0:
        print ("Gràcies i adéu")
        break
    factorial = 1
    i = 1
    
    while i <= nombre:
        factorial *= i
        i += 1
    
    print (f"El factorial del nombre {nombre} és {factorial}")