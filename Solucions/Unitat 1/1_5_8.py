punts = int(input("Quants punts hi ha en la teva targeta? "))

if punts >= 100:
    punts *= 1.15
    print("El teu bonus és de 15 %")

if punts < 100:
    punts *= 1.1
    print("El teu bonus és de 10 %")

print("Ara tens", punts, "punts")