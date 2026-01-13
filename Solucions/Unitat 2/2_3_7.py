donatiu = int(input ("Valor del donatiu: "))
impost = 0


if 5000 <= donatiu < 25000:
    impost = 100 + ((donatiu - 5000) * 0.08)
elif 25000 <= donatiu < 55000:
    impost = 1700 + ((donatiu - 25000) * 0.1)
elif 55000 <= donatiu < 200000:
    impost = 4700 + ((donatiu - 55000) * 0.12)
elif 200000 <= donatiu < 1000000:
    impost = 22100 + ((donatiu - 200000) * 0.15)
elif 1000000 <= donatiu:
    impost = 142100 + ((donatiu - 1000000) * 0.17)

if donatiu < 5000:
    print ("No hi ha impost!")
else:
    print (f"Import de l'impost: {impost}€.")