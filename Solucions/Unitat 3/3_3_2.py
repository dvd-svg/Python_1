frase = input("Escriu una frase: ")
cont = 0

while cont < len(frase):
    print (frase [cont])
    while cont < len(frase):
        if frase [cont] == " ":
            cont += 1
            break
        cont += 1