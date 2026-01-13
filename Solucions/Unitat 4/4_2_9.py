def nombre_mes_gran (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    if n3 > n2 and n3 > n1:
        return n3
    return n1

print(nombre_mes_gran(3, 4, 1))
print(nombre_mes_gran(99, -4, 7))
print(nombre_mes_gran(0, 0, 0))