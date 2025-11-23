def llegir_receptes(fitxer: str):
    receptes_raw = []
    
    with open (fitxer, encoding="utf-8") as nou_arxiu:
        for linia in nou_arxiu:
            receptes_raw.append(linia.strip())
    
    receptes = []
    
    recepta = {}
    nom = ""
    temps = 0
    ingredients = []
    
    for i in range(len(receptes_raw)):
        if i == 0 or receptes_raw [i - 1] == "":
            nom = receptes_raw [i]
            temps = int(receptes_raw [i + 1])
        elif i == 1 or receptes_raw [i - 2] == "":
            pass
        if receptes_raw != "":
            ingredients.append (receptes_raw [i])
        if receptes_raw [i] == "" or i == len(receptes_raw) - 1:
            recepta ["nom"] = nom
            recepta ["temps"] = temps
            recepta ["ingredients"] = ingredients
            receptes.append (recepta)
            nom = ""
            temps = 0
            ingredients = []
            recepta = {}    
    return receptes
            
def cercar_per_nom (fitxer: str, paraula: str):
    receptes = llegir_receptes(fitxer)
    resultats = []
    
    for recepta in receptes:
        if paraula in recepta ["nom"].lower():
            resultats.append (recepta ["nom"])
    
    return resultats

def cercar_per_temps (fitxer: str, temps_preparacio: int):
    receptes = llegir_receptes(fitxer)
    resultats = []    

    for recepta in receptes:
        if recepta ["temps"] == temps_preparacio:
            resultats.append (f"{recepta ['nom']}, temps de preparació {recepta ['temps']} min")
    
    return resultats

def cercar_per_ingredient(fitxer: str, ingredient_: str):
    receptes = llegir_receptes(fitxer)
    resultats = []    

    for recepta in receptes:
        for ingredient in recepta ["ingredients"]:
            if ingredient_ == ingredient:
                resultats.append (f"{recepta ['nom']}, temps de preparació {recepta ['temps']} min")
    
    return resultats


receptes_trobades = cercar_per_ingredient("receptes.txt", "ous")

for recepta in receptes_trobades:
    print(recepta)