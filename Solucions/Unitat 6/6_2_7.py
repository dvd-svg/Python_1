def afegir_paraula (paraula_eusk: str, paraula_cat: str):
    with open ("diccionari.txt", "a") as arxiu_diccionari:
        arxiu_diccionari.write(f"{paraula_eusk};{paraula_cat}\n")

def cercar (paraula: str):
    resultat = ""
    with open ("diccionari.txt") as arxiu_diccionari:
        for fila in arxiu_diccionari:
            valors = fila.strip().split(";")
            for valor in valors:
                if paraula == valor:
                    return f"{valors [0]} - {valors [1]}"
        return "no s'ha trobat aquest terme en el diccionari"

while True:
    print("1 - Afegir paraula, 2 - Cercar, 3 - Sortir")
    funcio = int(input ("Funció: "))
    if funcio == 3:
        print ("Fins aviat!")
        break
    if funcio == 1:
        paraula_eusk = input ("La paraula en euskera: ")
        paraula_cat = input ("La paraula en català: ")
        afegir_paraula (paraula_eusk, paraula_cat)
    elif funcio == 2:
        terme_cerca = input ("Terme de cerca: ")
        print (cercar (terme_cerca))
    print()