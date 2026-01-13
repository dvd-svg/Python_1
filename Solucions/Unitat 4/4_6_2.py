def caracter_mes_comu (cadena):
    
    repeticions = []
    
    for car in cadena:
        repeticions.append(cadena.count(car))
    
    for car in cadena:
        if cadena.count(car) == max(repeticions):
            return car
        
    



primera_cadena = "abcdbde"
print(caracter_mes_comu(primera_cadena))

segona_cadena = "exemplaryelementary"
print(caracter_mes_comu(segona_cadena))