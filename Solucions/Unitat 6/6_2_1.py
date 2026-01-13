nom = input ("A qui haig d'adreçar això: ")
arxiu = input ("On ho he de desar: ")

with open (arxiu, "w") as nou_arxiu:
    nou_arxiu.write (f"Hola {nom}, espero que gaudeixis aprenent Python! Salutacions")