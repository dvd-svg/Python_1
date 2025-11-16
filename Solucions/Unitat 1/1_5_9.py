print ("Quina és la previsió del temps per demà?")

temperatura = int(input("Temperatura: "))
pluja = input("Plourà (sí/no): ")

print ("Posa't texans i samarreta")
if temperatura < 20:
    print ("Et recomano un jersei també")
if temperatura < 10:
    print ("Porta't una jaqueta")
if temperatura < 5:
    print ("Millor un abric calent")
    print ("Crec que et caldran guants")
    
if pluja == "sí":
    print("No t'oblidis del paraigua!")