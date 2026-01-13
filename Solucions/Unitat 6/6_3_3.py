def filtrar_correctes (base_dades: str):
    resultat = []
    with open (base_dades) as arxiu_numeros:
        for fila in arxiu_numeros:
            valors = fila.strip().split(";")
            n_setmana = valors [0].split(" ") [1]
            numeros = valors [1].split(",")
            try:
                int(n_setmana)
            except:
                continue
            
            if len(numeros) != 7:
                continue
            
            incorrecte = False
            numeros_registrats = []
            
            for numero in numeros:
                try:
                    if int(numero) > 39 or int(numero) < 1 or int(numero) in numeros_registrats:
                        incorrecte = True
                        break
                except:
                    incorrecte = True
                    break
                
                numeros_registrats.append(int(numero))
            
            if incorrecte:
                continue
            
            resultat.append(fila.strip())
        
    with open ("numeros_correctes.csv", "w"):
        pass
        
    for fila in resultat:
        with open ("numeros_correctes.csv", "a") as arxiu_correctes:
            arxiu_correctes.write(f"{fila}\n")
            
filtrar_correctes("numeros_loteria.csv")
            
            