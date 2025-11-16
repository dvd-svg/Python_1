cadena = input ("Introdueix una cadena: ")
subcadena = input ("Introdueix una subcadena: ")

pos = cadena.find(subcadena)

if pos != -1:
    cadena = cadena [pos + len(subcadena):]
    pos2 = cadena.find(subcadena)
    
    if pos2 != -1:
        print (f"La segona aparició de la subcadena és a l'índex {pos + len(subcadena) + pos2}.")
    else:
        print ("La subcadena no apareix dues vegades dins la cadena.")
    
