from fractions import Fraction

def fraccionar (quantitat: int):
    fraccions = []
    for i in range(quantitat):
        fraccions.append (Fraction(1, quantitat))
    return fraccions

for p in fraccionar(3):
    print(p)

print()

print(fraccionar(5))