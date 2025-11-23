def juga_torn(tauler_joc: list, x: int, y: int, fitxa: str):
    if tauler_joc [y] [x] != "":
        return False
    tauler_joc [y] [x] = fitxa
    return True

tauler_joc = [["", "", ""], ["", "", ""], ["", "", ""]]
print(juga_torn(tauler_joc, 2, 0, "X"))
print(tauler_joc)