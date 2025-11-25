def llegir_entrada(missatge: str, minim: int, maxim: str):
    while True:
        try:
            numero = int(input(f"{missatge} "))
            if minim <= numero <= maxim:
                return numero
        except ValueError:
            pass
        print ("Has d'introduir un enter entre 5 i 10")
        
    return numero

numero = llegir_entrada("Si us plau, introdueix un número: ", 5, 10)
print("Has introduït:", numero)