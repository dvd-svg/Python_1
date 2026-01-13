def mes_llarga (cadenes: list):
    cadena_llarga = ""
    for cadena in cadenes:
        if len(cadena) > len(cadena_llarga):
            cadena_llarga = cadena
    return cadena_llarga

cadenes = ["hola", "hola!", "hello", "howdydoody", "hola tu"]
print(mes_llarga(cadenes))