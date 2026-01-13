def demanar_dades ():
    dades_finals = []    
    while True:
        entrada = input("Punts d'examen i exercicis completats: ")
        
        if entrada == "":
            break
        entrada_separada = entrada.split()
        print (entrada_separada)
        dades_finals.append(int(entrada_separada [0]))
        dades_finals.append(int(entrada_separada [1]))
    return dades_finals

def calcular_nota (examen, exercicis):
    nota_exercicis = exercicis // 10
    nota = nota_exercicis + examen
    if nota > 27:
        return 5
    if nota > 23:
        return 4
    if nota > 20:
        return 3
    if nota > 17:
        return 2
    if nota > 14:
        return 1
    return 0

def mitjana (notes):
    mitjana = sum(notes) / len (notes)
    print (f"Mitjana de punts: {mitjana: .2f}")

def percentatje_aprovats (notes):
    aprovats = 0
    for nota in notes:
        if nota >= 3:
            aprovats += 1
            
    percentatje_aprovats = 0
    if aprovats > 0:
        percentatje_aprovats = ((aprovats * 100) / len(notes))
    
    print (f"Percentatge d'aprovats: {percentatje_aprovats: .2f}")
    
def distribucio_notes (notes):
    freq_notes = [0, 0, 0, 0, 0, 0]
    
    for nota in notes:
        freq_notes [nota] += 1
    
    print (f"Distribució de notes:")

    for i in range(5, -1, -1):
        print (f"  {i}: ", end ="")
        for o in range (freq_notes [i]):
            print ("*", end="")
        print ("")

def estadistiques (llista):
    notes = []
    for i in range (0, len(llista) - 1, 2):
        nota = calcular_nota (llista [i], llista [i + 1])
        notes.append(nota)
    
    print ("Estadístiques:")
    
    mitjana (notes)
    percentatje_aprovats (notes)
    distribucio_notes(notes)
            
    
def main ():
    dades = demanar_dades()
    estadistiques (dades)

main()
    
