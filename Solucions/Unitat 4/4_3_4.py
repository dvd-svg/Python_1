llista = []
cont = 0

while True:
    paraula = input ("Paraula: ")
    if paraula in llista:
        print (f"Has escrit {cont} paraules diferents")
        break
    llista.append(paraula)
    cont += 1