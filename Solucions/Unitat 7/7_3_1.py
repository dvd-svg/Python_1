from datetime import datetime

dia_naixement = int(input("Dia: "))
mes_naixement = int(input("Mes: "))
any_naixement = int(input("Any: "))

data_naixement = datetime(any_naixement, mes_naixement, dia_naixement)
estrena_fortnite = datetime(2017, 7, 25)

if data_naixement < estrena_fortnite:
    edat_dia_fortnite = estrena_fortnite - data_naixement
    print (f"Teníes {edat_dia_fortnite.days} dies el dia de la publicació de Fortnite.")
else:
    print ("Encara no havies nascut el dia de la publicació de Fortnite.")
