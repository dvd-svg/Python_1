def tauler_escacs(longitud):
    i = 0
    while i < longitud:
        o = 0
        while o < longitud:
            if (i + o) % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")
            o += 1
        print("")
        i += 1

tauler_escacs(3)
print()
tauler_escacs(6)