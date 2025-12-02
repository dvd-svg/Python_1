from random import choice

def generar_contrasenya (longitud: int):
    contrasenya = ""
    caracters = "abcdefghijklmnopqrstuvwxyz"
    for i in range (longitud):
        contrasenya += choice(caracters)
        
    return contrasenya


for i in range(10):
    print(generar_contrasenya(8))