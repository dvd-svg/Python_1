nota = int(input("Quants punts [0-100]: "))

if nota < 0 or nota > 100:
    print ("Nota: impossible!")
elif 0 <= nota < 50:
    print ("Nota: suspès")
elif 50 <= nota < 60:
    print ("Nota: 1")
elif 60 <= nota < 70:
    print ("Nota: 2")
elif 70 <= nota < 80:
    print ("Nota: 3")
elif 80 <= nota < 90:
    print ("Nota: 4")
elif 90 <= nota <= 100:
    print ("Nota: 5")