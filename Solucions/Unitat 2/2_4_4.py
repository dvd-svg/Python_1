contrasenya = input("Contrasenya: ")

while True:
    contrasenya2 = input("Repeteix la contrasenya: ")
    if contrasenya == contrasenya2:
        print ("Compte d'usuari creat")
        break
    else:
        print ("No coincideixen!")