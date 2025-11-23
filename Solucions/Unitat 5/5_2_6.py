def transposa(matriu: list):
    nova_matriu = []
    
    for i in range (len(matriu)):
        nova_matriu.append([])
        for j in range(len (matriu [i])):
            nova_matriu [i].append (matriu [j] [i])
    
    return nova_matriu

matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print (transposa (matriu))