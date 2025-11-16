intents = 0
pin = 1234

while True:
    pin_usuari = int(input ("PIN: "))
    intents += 1
    if pin_usuari == pin:
        if intents == 1:
            print ("Correcte! Només has necessitat un únic intent")
        else:
            print (f"Correcte! has necessitat {intents} intents")
        break
    else:
        print("Incorrecte")