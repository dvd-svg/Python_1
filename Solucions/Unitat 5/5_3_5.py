agenda = {}

def cercar (diccionari: dict):
    nom = input ("nom: ")
    if nom in diccionari:
        for numero in diccionari [nom]:
            print (numero)
        return
    print ("no s'ha trobat el número")

def afegir (diccionari: dict):
    nom = input ("nom: ")
    numero = int(input("número: "))
    if nom in agenda:
        agenda [nom].append(numero)
    else:
        agenda [nom] = [numero]

while True:
    comanda = int(input("comanda (1 cercar, 2 afegir, 3 sortir): "))
    if comanda == 3:
        print ("sortint...")
        break
    if comanda == 1:
        cercar (agenda)
    elif comanda == 2:
        afegir (agenda)
        
    