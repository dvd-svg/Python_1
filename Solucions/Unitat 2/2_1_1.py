numero = int(input("Escriu un nombre: "))
if numero > 100:
    print("El nombre és més gran que cent")
    numero -= 100
    print("Ara el seu valor ha disminuït en cent")
    print("El seu valor ara és " + str(numero))
print(str(numero) + " deu ser el meu nombre de la sort!")
print("Que tinguis un bon dia!")