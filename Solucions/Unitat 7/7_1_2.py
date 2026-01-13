from string import ascii_letters, punctuation

def separar_caracters (text: str):
    lletres_ascii = ""
    puntuacio = ""
    altres = ""
    for lletra in text:
        if lletra in ascii_letters:
            lletres_ascii += lletra
        elif lletra in punctuation:
            puntuacio += lletra
        else:
            altres += lletra
            
    return (lletres_ascii, puntuacio, altres)

parts = separar_caracters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])