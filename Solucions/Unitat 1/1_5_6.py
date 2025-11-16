sou_hora = float(input("Sou per hora: "))
hores = int(input("Hores treballades: "))
dia = input("Dia de la setmana: ")

sou_dia = sou_hora * hores
if dia == "diumenge":
    sou_dia *= 2
print (f"Sou diari: {sou_dia} euros")
