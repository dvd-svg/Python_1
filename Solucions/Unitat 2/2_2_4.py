paraula1 = input("Escriu la 1a paraula: ")
paraula2 = input("Escriu la 2a paraula: ")

if paraula1 < paraula2:
    print (f"{paraula2} va última alfabèticament.")
elif paraula1 > paraula2:
    print (f"{paraula1} va última alfabèticament.")
else:
    print ("Has escrit la mateixa paraula dues vegades.")