paraula = input ("Introdueix una paraula: ")
caracter = input ("Introdueix un caracter: ")

while True:
    pos = paraula.find(caracter)
    if len(paraula) == 0:
        break
    if pos != -1:  
        if pos < (len(paraula)-2):
            print (paraula [pos: pos + 3])
            paraula = paraula[pos + 2:]
        else:
            break
    else:
        break