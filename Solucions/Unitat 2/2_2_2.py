nombre1 = int(input("Escriu el primer nombre: "))
nombre2 = int(input("Escriu un altre nombre: "))

if: nombre1 > nombre2:
    print(f"El nombre més gran és: {nombre1}")
elif nombre1 < nombre2:
    print(f"El nombre més gran és: {nombre2}")
else:
    print("Els nombres són iguals!")