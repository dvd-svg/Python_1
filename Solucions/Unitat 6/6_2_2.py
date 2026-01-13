def afegir (entrada: str):
    with open ("diari.txt", "a") as arxiu_diari:
        arxiu_diari.write(f"{entrada}\n")
    print()

def llegir():
    with open ("diari.txt") as arxiu_diari:
        print ("entrades:")
        print(arxiu_diari.read())

while True:
    print ("1 - afegir entrada, 2 - llegir entrades, 0 - sortir")
    funcio = int(input ("Funció: "))
    if funcio == 0:
        print ("Fins aviat!")
        break
    if funcio == 1:
        entrada = input ("Entrada del diari: ")
        afegir(entrada)
    elif funcio == 2:
        llegir()