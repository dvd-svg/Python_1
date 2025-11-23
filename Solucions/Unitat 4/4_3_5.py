llista = []
cont = 0

while True:
    element = int(input("Nou element: "))
    if element == 0:
        print ("Adéu!")
        break
    llista.append(element)
    print (f"La llista ara és {llista}")
    print (f"La llista en ordre és {sorted(llista)}")