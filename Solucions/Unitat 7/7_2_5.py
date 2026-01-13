from random import sample

def paraules(n: int, principi: str):
    llista_sencera= []
    
    with open ("paraules.txt") as arxiu_paraules:
        for fila in arxiu_paraules:
            valor = fila.strip()
            if valor.startswith(principi) and not(valor in llista_sencera):
                llista_sencera.append (valor)
                
    if len(llista_sencera) < n:
        raise ValueError (f"Hi ha menys de {n} paraules que comencin per {principi}")
    
    return sample (llista_sencera, n)

llista_paraules = paraules(3, "ca")
for paraula in llista_paraules:
    print(paraula)