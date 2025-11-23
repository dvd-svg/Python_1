def linia (cops, cadena):
    if cadena == "":
        cadena = "*"
    print (cadena [0] * cops)

def quadrat_de_coixinets (mida):
    i = 0
    while i < mida:
        linia (mida, "#")
        i += 1

quadrat_de_coixinets(5)
print()
quadrat_de_coixinets(3)