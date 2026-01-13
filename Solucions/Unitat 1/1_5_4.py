nombre = int(input("Introdueix un nombre:"))

if nombre < 1000:
    print ("Aquest nombre és menor que 1000")
    if nombre < 100:
        print ("Aquest nombre és menor que 100")
        if nombre < 10:
            print ("Aquest nombre és menor que 10")

print ("Gràcies!")