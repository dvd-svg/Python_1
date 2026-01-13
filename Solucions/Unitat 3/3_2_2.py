cadena1 = input("Introdueix la cadena 1: ")
cadena2 = input("Introdueix la cadena 2: ")

if len(cadena1) > len(cadena2):
    print (f"{cadena1} és la cadena més llarga")
elif len(cadena1) < len(cadena2):
    print (f"{cadena2} és la cadena més llarga")
else:
    print ("Les cadenes tenen la mateixa longitud")

