cadena = input("Introdueix una cadena: ")

segon_car = cadena [1]
penultim_car = cadena [len(cadena) - 2]

if segon_car == penultim_car:
    print (f"El segon i penúltim caràcter són {segon_car}")
else:
    print (f"El segon i penúltim caràcter són diferents")