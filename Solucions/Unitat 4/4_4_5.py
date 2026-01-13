def palindrom (paraula):
    i = len(paraula) - 1
    for o in range(len(paraula)):
        if paraula [i] != paraula [o]:
            return False
        i -= 1
    return True

while True:
    paraula_entrada = input ("Si us plau, introdueix un palíndrom: ")
    if palindrom (paraula_entrada):
        print (f"{paraula_entrada} és un palíndrom")
        break
    print ("això no era un palíndrom")