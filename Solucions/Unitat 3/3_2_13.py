paraula = input ("Introdueix una paraula: ")
caracter = input ("Introdueix un caracter: ")

if caracter in paraula:
    pos = paraula.find(caracter)
    if pos < (len(paraula)-2):
        print (paraula [pos: pos + 3])