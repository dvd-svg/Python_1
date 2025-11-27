from math import sqrt

def hipotenusa (catet1: float, catet2: float):
    return (sqrt(catet1**2 + catet2**2))

print(hipotenusa(3,4)) # 5.0
print(hipotenusa(5,12)) # 13.0
print(hipotenusa(1,1)) # 1.4142135623730951