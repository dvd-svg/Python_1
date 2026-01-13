def sense_vocals (cadena):
    cadena = cadena.replace("a", "")
    cadena = cadena.replace("e", "")
    cadena = cadena.replace("i", "")
    cadena = cadena.replace("o", "")
    cadena = cadena.replace("u", "")
    return cadena

cadena_exemple = "aixo es un exemple"
print(sense_vocals(cadena_exemple))
