from random import choice, shuffle

def generar_contrasenya_forta(longitud: int, te_nombres: bool, te_caracters_especials: bool):
    lletres = "abcdefghijklmnopqrstuvwxyz"
    nombres = "0123456789"
    especials = "!?=+-()#"
    
    contrasenya = [choice(lletres)]

    caracters_minims = 1
    
    if te_nombres:
        contrasenya.append(choice(nombres))
        caracters_minims += 1

    if te_caracters_especials:
        contrasenya.append(choice(especials))
        caracters_minims += 1
    
    if longitud < caracters_minims:
        raise ValueError("Amb els paràmetres seleccionats la longitud mínima de la contrasenya és de " + str(caracters_minims) + " caràcters")

    conjunt = lletres
    if te_nombres:
        conjunt += nombres
    if te_caracters_especials:
        conjunt += especials

    while len(contrasenya) < longitud:
        contrasenya.append(choice(conjunt))

    shuffle(contrasenya)
    
    cadena_contrasenya = ""
    
    for caracter in contrasenya:
        cadena_contrasenya += caracter
    
    return cadena_contrasenya


for i in range(10):
    print(generar_contrasenya_forta(7, True, True))
