def formatejada (llista):
    nova_llista = []
    for element in llista:
        nova_llista.append(f"{element:.2f}")
    return nova_llista

llista_nombres = [1.234, 0.3333, 0.11111, 3.446]
nova_llista = formatejada(llista_nombres)
print(nova_llista)