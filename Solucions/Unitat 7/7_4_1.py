import json

def imprimir_persones (arxiu: str):
    with open (arxiu, encoding="utf-8") as arxiu_persones:
        dades = arxiu_persones.read()
        
    persones = json.loads(dades)
    
    for persona in persones:
        aficions = ""
        for aficio in persona ["aficions"]:
            aficions += f", {aficio}"
        aficions = aficions.lstrip(", ")
        print (f'{persona ["nom"]} {persona ["edat"]} anys ({aficions})')
        
imprimir_persones ("persones.json")