def primera_paraula (frase_entrada):
    paraula = ""
    i = 0
    while True:
        caracter = frase_entrada [i]
        if caracter == " ":
            break
        paraula += caracter
        i += 1
    return paraula

def segona_paraula (frase_entrada):
    paraula = ""
    i = frase_entrada.find(" ") + 1
    while True:
        caracter = frase_entrada [i]
        if caracter == " ":
            break
        paraula += caracter
        i += 1
    return paraula

def ultima_paraula (frase_entrada):
    paraula = ""
    i = len(frase_entrada) - 1
    while True:
        caracter = frase_entrada [i]
        if caracter == " ":
            i += 1
            break
        i -= 1
    while i < len(frase_entrada):
        caracter = frase_entrada [i]
        if caracter == " ":
            break
        paraula += caracter
        i += 1
    return paraula

frase = "era una nit fosca i tempestuosa python"
print(primera_paraula(frase))
print(segona_paraula(frase))
print(ultima_paraula(frase))