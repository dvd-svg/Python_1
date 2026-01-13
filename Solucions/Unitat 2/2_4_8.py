print ("Introdueix nombres enters. Escriu 0 per acabar.")

count = 0
suma = 0
positius = 0
negatius = 0

while True:
    nombre = int(input("Nombre: "))
    if nombre == 0:
        break
    elif nombre > 0:
        positius += 1
    elif nombre < 0:
        negatius += 1
    count += 1
    suma += nombre
    
print (f"Nombres introduïts: {count}")
print (f"La suma dels nombres és {suma}")
print (f"La mitjana dels nombres és {suma / count}")
print (f"Nombres positius: {positius}")
print (f"Nombres negatius: {negatius}")