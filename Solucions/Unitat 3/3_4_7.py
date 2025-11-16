def quadrat_text(text, mida):
    i = 0
    cont = 0
    while i < mida:
        o = 0
        while o < mida:
            if cont == len(text):
                cont = 0
            print (text [cont], end="")
            o += 1
            cont +=1
        print ("")
        i += 1

quadrat_text("ab", 3)
print()
quadrat_text("aybabtu", 5)