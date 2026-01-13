def avet (mida):
    i = mida - 1
    arbre = "*"
    while i >= 0:
        print (" " * i + arbre )
        i -= 1
        arbre += "**"
    print (" " * (mida - 1) + "*")



avet(3)
print ("")
avet(5)
