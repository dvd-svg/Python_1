def no_cridar (llista):
    llista_minuscula = []
    for cadena in llista:
        if not (cadena == "" or cadena.isupper()):
            llista_minuscula.append(cadena)
    return llista_minuscula


llista_textos = ["ABC", "def", "MAJUSCULA", "ALTRA MAJUSCULA", "minúscula", "una altra minúscula", "Majuscula"]
llista_podada = no_cridar(llista_textos)
print(llista_podada)
