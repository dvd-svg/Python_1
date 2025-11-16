any = int(input("Introdueix un any: "))

if any % 4 == 0 and (any % 100 != 0 or any % 400 == 0):
    print ("Aquest any és de traspàs.")
else:
    print ("Aquest any no és de traspàs.")
    
