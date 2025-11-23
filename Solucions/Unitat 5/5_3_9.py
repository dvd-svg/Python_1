def trobar_pelicules(base_dades: list, terme_cerca: str):
    pelicules_trobades = []
    for pelicula in base_dades:
        if terme_cerca in pelicula ["nom"]:
            pelicules_trobades.append(pelicula)
    return pelicules_trobades

def afegir_pelicula(base_dades: list, nom_: str, director_: str, any_: int, durada_: int):
    pelicula = {"nom" : nom_, "director" : director_ , "any" : any_}
    base_dades.append(pelicula)
    
    
    
    
base_dades = [{"nom": "Allò que el vent s'endugué amb Python", "director": "Víctor Pything", "any": 2017, "durada": 116},
{"nom": "Pythons en un avió", "director": "Renat Pytholin", "any": 2001, "durada": 94},
{"nom": "L'alba dels programadors morts", "director": "M. Nit Python", "any": 2011, "durada": 101}]

les_meves_pelicules = trobar_pelicules(base_dades, "Python")
print(les_meves_pelicules)