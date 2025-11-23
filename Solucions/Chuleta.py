# PROGRAMA DE PRACTICA PER A FUNCIONS BÀSIQUES DE PYTHON

print("=== FUNCIONS PER A CADENES DE TEXT ===")

cadena = "Hola món"
print (f"Cadena: {cadena}")

# len() - Retorna la longitud d'una cadena o llista
print(f"len('{cadena}') = {len(cadena)}")  # Resultat: Hola món = 9


# cadena [a:b] - Retorna una subcadena des de l'índex a fins b (b no inclòs)
print(f"cadena[2:6] = '{cadena[2:6]}'")  # Resultat: 'la m'


# char in cadena - Comprova si un caràcter està en la cadena
print(f"'a' in cadena = {'a' in cadena}")  # Resultat: 'a' in cadena = True
print(f"'x' in cadena = {'x' in cadena}")  # Resultat: 'x' in cadena = False


# find() - Cerca un substring i retorna la posició (-1 si no el troba)
print(f"cadena.find('món') = {cadena.find('món')}")  # Resultat: cadena.find('món') = 5
print(f"cadena.find('Python') = {cadena.find('Python')}")  # Resultat: cadena.find('món') = -1


print ("")
print ("")
#--------------------------------------------------------------------------------------------------

print("\n=== FUNCIONS PER A LLISTES ===")


# list() - Converteix un rang en llista
llista_nums = list(range(5))  # range(0:5:1) és equivalent a range(5)
print(f"list(range(5)) = {llista_nums}")  # Resultat: list(range(5)) = [0, 1, 2, 3, 4]


# append() - Afegeix un element al final de la llista
llista = [1, 2, 3]
print (f"Llista: {llista}")
llista.append(4)
print(f"Després d'append(4): {llista}")  # Resultat: Després d'append(4): [1, 2, 3, 4]


# insert(i, a) - Insereix un element a la posició i
llista.insert(1, 99)
print(f"Després d'insert(1, 99): {llista}")  # Resultat: Després d'insert(1, 99): [1, 99, 2, 3, 4]


# pop() - Elimina i retorna l'últim element (o l'element a l'índex especificat)
element = llista.pop()
print(f"Element eliminat amb pop(): {element}")  # Resultat: 4
print(f"Llista després de pop(): {llista}")  # Resultat: Llista després de pop(): [1, 99, 2, 3]


# remove() - Elimina la primera ocurrencia d'un element
llista.remove(99)
print(f"Després de remove(99): {llista}")  # Resultat: Després de remove(99): [1, 2, 3]


print ("")
print ("")
#--------------------------------------------------------------------------------------------------

print("\n=== ORDENACIÓ DE LLISTES ===")

# .sort() - Ordena la llista original (modifica la llista)
llista_desordenada = [3, 1, 4, 1, 5, 9, 2]
llista_desordenada.sort()
print(f"Llista original després de .sort(): {llista_desordenada}")  # Resultat: Llista original després de .sort(): [1, 1, 2, 3, 4, 5, 9]

# sorted(list) - Retorna una nova llista ordenada (no modifica l'original)
llista_original = [5, 2, 8, 1, 9]
llista_ordenada = sorted(llista_original)
print(f"Llista original: {llista_original}")  # Resultat: Llista original: [5, 2, 8, 1, 9]
print(f"sorted(llista): {llista_ordenada}")  # Resultat: sorted(llista): [1, 2, 5, 8, 9]


print ("")
print ("")
#--------------------------------------------------------------------------------------------------

print("\n=== FUNCIONS MATEMÀTIQUES PER A LLISTES ===")

# max() - Retorna el valor màxim
# min() - Retorna el valor mínim
# sum() - Retorna la suma de tots els elements
nums = [10, 20, 5, 35, 15]
print (f"nums = {nums}")
print(f"max({nums}) = {max(nums)}")  # Resultat: max({nums}) = 35
print(f"min({nums}) = {min(nums)}")  # Resultat: min({nums}) = 5
print(f"sum({nums}) = {sum(nums)}")  # Resultat: sum({nums}) = 85

print ("")
print ("")
#--------------------------------------------------------------------------------------------------

print("\n=== BUCLES FOR ===")

# for char in cadena - Recorre cada caràcter d'una cadena
print("Bucle for char in cadena:")
for char in "Hola":
    print(f"  Caràcter: {char}")  #Caràcter: H
                                  #Caràcter: o
                                  #Caràcter: l
                                  #Caràcter: a

# for i in range() - Bucle amb rang numèric
print("Bucle for i in range(3):")
for i in range(3):
    print(f"  i = {i}")  #i = 0
                         #i = 1
                         #i = 2
    
# range(2, 7) - De 2 a 7 (exclòs)
print("Bucle for i in range(2, 7):")
for i in range(2, 7):
    print(f"  i = {i}")  # i = 2
                         # i = 3
                         # i = 4
                         # i = 5
                         # i = 6
        
        
# range(1, 10, 2) - De 1 a 10 (exclòs) amb increments de 2
print("Bucle for i in range(1, 10, 2):")
for i in range(1, 10, 2):
    print(f"  i = {i}")  # i = 1
                         # i = 3
                         # i = 5
                         # i = 7
                         # i = 9
                         

# range(5, 0, -1) de 5 a 0 (exclòs) amb increment de 1 negatiu (compte enrere)
print("Bucle for i in range(5, 0, -1):")
for i in range(5, 0, -1):
    print(f"  i = {i}")  # i = 5
                         # i = 4
                         #i =  3
                         #i =  2
                         #i = 1

print ("")
print ("")
#--------------------------------------------------------------------------------------------------

print("\n=== SLICING (REBANADES) DE LLISTES ===")

llista_completa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list [1:3] - Elements des de l'índex 1 fins 3 (3 no inclòs)
print(f"llista[1:3] = {llista_completa[1:3]}")  # Resultat: llista[1:3] = [1, 2]

#list [0:8:2] - Elements des de l'índex 0 fins 8 progressant de 2 en 2
print(f"llista[0:8:2] = {llista_completa[0:8:2]}")  # Resultat: llista[0:8:2] = [0, 2, 4, 6]

# list[6:1:-1] - Elements des de 6 fins 1 en ordre invers
print(f"llista[6:1:-1] = {llista_completa[6:1:-1]}")  # Resultat: llista[6:1:-1] = [6, 5, 4, 3, 2]

# list[::-1] - Tota la llista en ordre invers
print(f"llista[::-1] = {llista_completa[::-1]}")  # Resultat: llista[::-1] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print ("")
print ("")
#--------------------------------------------------------------------------------------------------
