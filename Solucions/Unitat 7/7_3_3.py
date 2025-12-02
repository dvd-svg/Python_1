from datetime import datetime, timedelta

nom_fitxer = input("Nom del fitxer: ")
data_inici = datetime.strptime(input("Data d'inici (dd.mm.yyyy): "), "%d.%m.%Y")
n_dies = int(input("Quants dies: "))
dia_actual = data_inici

informacio_pantalla = [] 

for i in range(n_dies):
    entrada = input(f"Temps de pantalla {dia_actual.strftime('%d.%m.%Y')}: ")
    entrada_separada = entrada.split (" ")
    minuts_dia = []
    for j in range(len(entrada_separada)):
        minuts_dia.append (int(entrada_separada[j]))

    informacio_pantalla.append(minuts_dia)
    dia_actual += timedelta(days=1)

with open(nom_fitxer, "w") as fitxer:
    fitxer.write(f"Període de temps: {data_inici.strftime('%d.%m.%Y')} - {dia_actual.strftime('%d.%m.%Y')}\n")

    minuts_totals = 0
    for dia in informacio_pantalla:
        minuts_totals += sum(dia)
    fitxer.write(f"Minuts totals: {minuts_totals}\n")
    
    fitxer.write(f"Minuts promig: {minuts_totals / (3 * n_dies)}\n")
    
    dia_actual = data_inici
    for info_dia in informacio_pantalla:
        fitxer.write(f"{dia_actual.strftime('%d.%m.%Y')}: {info_dia[0]}/{info_dia[1]}/{info_dia[2]}\n")
    
    
    