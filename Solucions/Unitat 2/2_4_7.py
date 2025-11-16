historia = ""
darrera_paraula = ""

while True:
    paraula = input ("Introdueix una paraula: ")
    if paraula == "final":
        historia += f" {darrera_paraula}"
        break
    elif paraula == darrera_paraula:
        break
    elif paraula != "":
        historia += f" {darrera_paraula}"
        darrera_paraula = paraula

print (historia)
