agenda = {}

def cercar (diccionari: dict):
    nom = input ("nom: ")
    if nom in diccionari:
        print (f"número: {diccionari [nom]}")
        return
    print ("no s'ha trobat el número")

def afegir (diccionari: dict):
    nom = input ("nom: ")
    numero = int(input("número: "))
    agenda [nom] = numero

while True:
    comanda = int(input("comanda (1 cercar, 2 afegir, 3 sortir): "))
    if comanda == 3:
        print ("sortint...")
        break
    if comanda == 1:
        cercar (agenda)
    elif comanda == 2:
        afegir (agenda)
        
    