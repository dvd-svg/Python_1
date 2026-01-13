def emmagatzema_dades_personals(persona: tuple):
    with open ("persones.csv", "a") as arxiu_persones:
        arxiu_persones.write (f"{persona [0]}:{persona [1]};{persona [2]}\n")
        

emmagatzema_dades_personals (("Pau Paulson", 37, 175.5))