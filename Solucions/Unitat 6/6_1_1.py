def mes_gran (arxiu):
    with open (arxiu) as nou_arxiu:
        max = -9999999999999999
        for num in nou_arxiu:
            num_tractat = int(num.replace("\n", ""))
            if int(num_tractat > max):
                max = num_tractat
        return max
    
    
print (mes_gran("6_1_1.txt"))