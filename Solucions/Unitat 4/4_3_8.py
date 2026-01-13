def rang_de_llista (llista_entrada):
    return max(llista_entrada) - min (llista_entrada)

llista = [1, 2, 3, 4, 5]
resultat = rang_de_llista(llista)
print("El rang de la llista és", resultat)