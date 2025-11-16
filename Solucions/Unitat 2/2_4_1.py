from math import sqrt

while True:
    numero = int(input("Introdueix un número: "))
    if numero  < 0:
        print ("Número invàlid")
    elif numero == 0:
        print ("sortint...")
        break
    else:
        print (sqrt(numero))