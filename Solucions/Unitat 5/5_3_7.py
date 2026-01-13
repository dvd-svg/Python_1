unitats = {0 : "zero", 1 : "u", 2 : "dos", 3 : "tres", 4 : "quatre", 5 : "cinc", 6 : "sis", 7 : "set", 8 : "vuit", 9 : "nou"}
desenes = {2 : "vint", 3 : "trenta", 4 : "quaranta", 5 : "cinquanta", 6 : "seixanta", 7 : "setanta", 8 : "vuitanta", 9 : "noranta"}
especials = {10 : "deu", 11 : "onze", 12 : "dotze", 13 : "tretze", 14 : "catorze", 15 : "quinze", 16 : "setze", 17 : "diset", 18 : "divuit", 19: "dinou"}

def diccionari_nombres ():
    diccionari_final = {}
    for i in range (100):
        if i < 10:
            diccionari_final [i] = unitats [i]
        elif 10 < i and i % 10 == 0:
            diccionari_final [i] = desenes [i // 10]
        elif 9 < i < 20:
            diccionari_final [i] = especials [i]
        elif 20 < i < 30:
            diccionari_final [i] = f"{desenes [i // 10]}-i-{unitats [i % 10]}"
        elif 30 < i < 100 and i % 10 != 0:
            diccionari_final [i] = f"{desenes [i // 10]}-{unitats [i % 10]}"
                
    return diccionari_final

print (diccionari_nombres())