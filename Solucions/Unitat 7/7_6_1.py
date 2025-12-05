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
            if termes [1] in noms_variables:
                resultats.append (variables[termes [1]])
            else:
                resultats.append (termes [1])
        elif "MOV" in instruccio:
            if termes [2] in noms_variables:
                variables [termes [1]] = variables[termes [2]]
            else:
                variables [termes [1]] = int(termes [2])
        
        elif "ADD" in instruccio:
            if termes [2] in noms_variables:
                variables [termes [1]] += variables [termes [2]]
            else:
                variables [termes [1]] += int(termes [2])
        elif "SUB" in instruccio:
            if termes [2] in noms_variables:
                variables [termes [1]] -= variables [termes [2]]
            else:
                variables [termes [1]] -= int(termes [2])
        elif "MUL" in instruccio:
            if termes [2] in noms_variables:
                variables [termes [1]] *= variables [termes [2]]
            else:
                variables [termes [1]] *= int(termes [2])
        
        elif termes [0] == "JUMP":
            i = instruccions.index (termes [1]+":")
            continue
        
        elif "IF" in instruccio:
            if termes [2] == '==':
                if termes [3] in noms_variables:
                    if variables [termes [1]] == variables [termes [3]]:
                        i = instruccions.index (termes [5]+":")
                elif variables [termes [1]] == int(termes [3]):
                    i = instruccions.index (termes [5]+":")
            elif termes [2] == '!=':
                if termes [3] in noms_variables:
                    if variables [termes [1]] != variables [termes [3]]:
                        i = instruccions.index (termes [5]+":")
                elif variables [termes [1]] != int(termes [3]):
                    i = instruccions.index (termes [5]+":")
            elif termes [2] == '<':
                if termes [3] in noms_variables:
                    if variables [termes [1]] < variables [termes [3]]:
                        i = instruccions.index (termes [5]+":")
                elif variables [termes [1]] < int(termes [3]):
                    i = instruccions.index (termes [5]+":")
            elif termes [2] == '<=':
                if termes [3] in noms_variables:
                    if variables [termes [1]] <= variables [termes [3]]:
                        i = instruccions.index (termes [5]+":")
                elif variables [termes [1]] <= int(termes [3]):
                    i = instruccions.index (termes [5]+":")
            elif termes [2] == '>':
                if termes [3] in noms_variables:
                    if variables [termes [1]] > variables [termes [3]]:
                        i = instruccions.index (termes [5]+":")
                elif variables [termes [1]] > int(termes [3]):
                    i = instruccions.index (termes [5]+":")
            elif termes [2] == '>=':
                if termes [3] in noms_variables:
                    if variables [termes [1]] >= variables [termes [3]]:
                        i = instruccions.index (termes [5]+":")
                elif variables [termes [1]] >= int(termes [3]):
                    i = instruccions.index (termes [5]+":")
        
        elif "END" in instruccio:
            break
    
        i += 1
    
    return resultats

programa4 = []
programa4.append("MOV N 50")
programa4.append("PRINT 2")
programa4.append("MOV A 3")
programa4.append("inici:")
programa4.append("MOV B 2")
programa4.append("MOV Z 0")
programa4.append("prova:")
programa4.append("MOV C B")
programa4.append("nou:")
programa4.append("IF C == A JUMP error")
programa4.append("IF C > A JUMP sobre")
programa4.append("ADD C B")
programa4.append("JUMP nou")
programa4.append("error:")
programa4.append("MOV Z 1")
programa4.append("JUMP sobre2")
programa4.append("sobre:")
programa4.append("ADD B 1")
programa4.append("IF B < A JUMP prova")
programa4.append("sobre2:")
programa4.append("IF Z == 1 JUMP sobre3")
programa4.append("PRINT A")
programa4.append("sobre3:")
programa4.append("ADD A 1")
programa4.append("IF A <= N JUMP inici")
resultat = run(programa4)
print(resultat)