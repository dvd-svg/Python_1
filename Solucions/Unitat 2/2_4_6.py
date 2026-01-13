any = int(input("Any: "))
proper_any = any + 1

while True:
    if proper_any % 4 == 0:
        if proper_any % 100 == 0:
            if proper_any % 400 == 0:
                break
        else:
            break
    proper_any += 1

print (f"El proper any de traspas després de {any} és {proper_any}")