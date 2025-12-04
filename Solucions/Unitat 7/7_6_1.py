def run (instruccions: list):
    i = 0
    resultats = []
    
    noms_variables = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    variables = {}
    for nom_variable in noms_variables:
        variables [nom_variable] = 0
    while i < len(instruccions):
        
        
        
        instruccio = instruccions [i]
        termes = instruccio.split (" ")
        
        if "PRINT" in instruccio:
            resultats.append (variables[termes [1]])
        elif "MOV" in instruccio:
            variables [termes [1]] = int(termes [2])
        elif "ADD" in instruccio:
            pass
        elif "SUB" in instruccio:
            pass
        elif "MUL" in instruccio:
            pass
        elif "JUMP" in instruccio:
            i = instruccions.index (termes [1])
            continue
        elif "IF" in instruccio:
            pass
        elif "END" in instruccio:
            break
    
        i += 1
    
    return resultats

programa1 = []
programa1.append("MOV A 1")
programa1.append("MOV B 2")
programa1.append("PRINT A")
programa1.append("PRINT B")
programa1.append("ADD A B")
programa1.append("PRINT A")
programa1.append("END")
resultat = run(programa1)
print(resultat)