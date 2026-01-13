def afegir_estudiant (base_dades: dict, estudiant: str): 
    if estudiant in base_dades:
        print ("Aquest estudiant ja està registrat")
    else:
        base_dades [estudiant] = []
    
    
def imprimir_estudiant (base_dades: dict, estudiant: str):
    print (f"{estudiant}:")
    
    if estudiant not in base_dades:
        print("no hi ha aquesta persona a la base de dades")
        return
    
    cursos = base_dades[estudiant]
    
    if cursos == []:
        print ("cap curs completat")
        return
    
    cursos_completats = []
    noms = []
    notes = []
    
    for nom, nota in cursos:
        if nota != 0 and nom not in noms:
            cursos_completats.append((nom, nota))
            noms.append(nom)
            notes.append(nota)
                    
    print (f"{len(cursos_completats)} cursos completats:")
    
    for nom, nota in cursos_completats:
        print (f" {nom} {nota}")
    
    print (f"nota mitjana {sum(notes) / len(notes)}")  
    


def afegir_curs(base_dades: dict, estudiant: str, curs: tuple):
    nom, nota = curs
    if estudiant in base_dades and nota != 0:
        base_dades[estudiant].append((nom, nota))



def resum(base_dades):
    max_cursos = ("ningu", 0)
    max_mitjana = ("ningu", 0)
    
    for estudiant in base_dades:
        noms = []
        notes = []
        
        for nom, nota in base_dades[estudiant]:
            if nota != 0 and nom not in noms:
                noms.append(nom)
                notes.append(nota)
        
        num_cursos = len(notes)
        
        if num_cursos > max_cursos[1]:
            max_cursos = (estudiant, num_cursos)
        
        if num_cursos > 0:
            mitjana = sum(notes) / num_cursos
            if mitjana > max_mitjana[1]:
                max_mitjana = (estudiant, mitjana)
    
    print (f"estudiants {len(base_dades)}")                
    print (f"més cursos completats {max_cursos [1]} {max_cursos [0]}")
    print (f"millor nota mitjana {max_mitjana [1]} {max_mitjana [0]}")



estudiants = {}
afegir_estudiant(estudiants, "Pere")
afegir_estudiant(estudiants, "Elisabet")
afegir_curs(estudiants, "Pere", ("Estructures de Dades i Algorismes", 1))
afegir_curs(estudiants, "Pere", ("Introducció a la Programació", 1))
afegir_curs(estudiants, "Pere", ("Curs Avançat de Programació", 1))
afegir_curs(estudiants, "Elisabet", ("Introducció a la Programació", 5))
afegir_curs(estudiants, "Elisabet", ("Introducció a la Informàtica", 4))
resum(estudiants)