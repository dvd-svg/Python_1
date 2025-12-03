from ajudant_text import canviar_majuscules, dividir_meitat, eliminar_caracters_especials

meu_text = "Hola, com estàs!"

print(canviar_majuscules(meu_text))

p1, p2 = dividir_meitat(meu_text)

print(p1)
print(p2)

m2 = eliminar_caracters_especials("Això és una prova, vejam com va!!!11!")
print(m2)