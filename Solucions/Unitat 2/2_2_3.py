print ("Persona 1:")
nom1 = input("Nom: ")
edat1= int(input("Edat: "))

print ("Persona 2:")
nom2 = input("Nom: ")
edat2= int(input("Edat: "))

if edat1 < edat2:
    print (f"La persona més gran és {nom2}")
elif edat1 > edat2:
    print (f"La persona més gran és {nom1}")
else:
    print (f"{nom1} i {nom2} tenen la mateixa edat")
