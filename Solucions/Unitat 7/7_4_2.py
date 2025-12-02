import urllib.request
import json

def recuperar_tot ():
    peticio = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses").read()
    cursos = json.loads(peticio)

    cursos_actius = []

    for curs in cursos:
        if curs ['enabled'] == True:
            nom = curs ['fullName']
            codi = curs ['name']
            any_ = curs ['year']
            exercicis = curs ['exercises']
            suma_exercicis = 0
            for exercici in exercicis:
                suma_exercicis += exercici
            
            cursos_actius.append ((nom, codi, any_, suma_exercicis))

    return cursos_actius

def recuperar_curs (nom: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{nom}/stats"
    peticio = urllib.request.urlopen (url).read()
    info_curs = json.loads(peticio)
    
    setmanes = len(info_curs)
    alumnes = 0
    hores = 0
    exercicis = 0
    
    for setmana, dades in info_curs.items():
        alumnes += dades ["students"]
        hores += dades ["hour_total"]
        exercicis += dades ["exercise_total"]
    
    mitjana_hores = hores / setmanes
    mitjana_exercicis = exercicis / setmanes
    
    return {"setmanes": setmanes, "alumnes": alumnes, "hores": hores, "mitjana_hores": mitjana_hores, "exercicis": exercicis, "mitjana_exercicis": mitjana_exercicis}

print (recuperar_curs ("docker2019"))