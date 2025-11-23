llista = []
cont = 1

while True:
    print (f"La llista és {llista}")
    menu = input ("(a)fegir, (e)liminar o (s)ortir: ")
    if menu == "s":
        print ("Adéu!")
        break
    if menu == "a":
        llista.append(cont)
        cont += 1
    elif menu == "e":
        cont -= 1
        llista.remove(cont)
        