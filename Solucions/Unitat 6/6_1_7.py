frase = input("Escriu text: ")

paraules = frase.split(" ")
print()

for paraula in paraules:
    paraula_in_paraules = False
    with open ("llista_paraules.txt", encoding="utf-8") as nou_arxiu:
        for linia in nou_arxiu:
            paraula_diccionari = linia.strip()
            if paraula.lower() == paraula_diccionari:
                paraula_in_paraules = True
                break
    if paraula_in_paraules:
        print (f"{paraula} ", end="")
    else:
        print (f"*{paraula}* ", end="")