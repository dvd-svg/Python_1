def crear_tupla(x: int, y: int, z: int):
    menor = min (x, y, z)
    major = max (x, y, z)
    suma = x + y + z
    return (menor, major, suma)


print(crear_tupla(5, 3, -1))