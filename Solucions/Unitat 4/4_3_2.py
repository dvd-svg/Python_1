llista = []

n_elements = int(input("Quants elements vols afegir: "))

i = 1

while i <= n_elements:
    element = int(input("Element {i}: "))
    llista.append(element)
    i += 1
    
print (llista)