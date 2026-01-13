def afegir_pelicula(base_dades: list, nom_: str, director_: str, any_: int, durada_: int):
    pelicula = {"nom" : nom_, "director" : director_ , "any" : any_}
    base_dades.append(pelicula)
    
    
    
    
base_dades = []
afegir_pelicula(base_dades, "Allò que el vent s'endugué amb Python", "Víctor Pything", 2017, 116)
afegir_pelicula(base_dades, "Pítons en un avió", "Renat Pytholin", 2001, 94)
print(base_dades)