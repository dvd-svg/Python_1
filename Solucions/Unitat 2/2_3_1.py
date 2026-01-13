edat = int(input("Quna edat tens?"))


if edat < 0:
    print ("Això deu ser un error.")
elif edat < 5:
    print ("sospito que encara no saps escriure...")
elif edat > 116:
    print ("no crec que encara puguis escriure emb aquesta edat...")
else:
    print (f"D'acord, tens {edat} anys.")