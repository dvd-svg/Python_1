def linia (cops, cadena):
    if cadena == "":
        cadena = "*"
    print (cadena [0] * cops)

def caixa_de_coixinets (mida):
    i = 0
    while i < mida:
        linia (10, "#")
        i += 1

caixa_de_coixinets(5)
print()
caixa_de_coixinets(2)