lletra1 = input ("1a lletra: ")
lletra2 = input ("2a lletra: ")
lletra3 = input ("3a lletra: ")

if lletra1 <= lletra2 <= lletra3 or lletra3 <= lletra2 <= lletra1:
    print (f"La lletra del mig és {lletra2}")
elif lletra2 <= lletra1 <= lletra3 or lletra3 <= lletra1 <= lletra2:
    print (f"La lletra del mig és {lletra1}")
else:
    print (f"La lletra del mig és {lletra3}")