def nombres_diferents (llista):
    diferents = []
    for num in llista:
        if not (num in diferents):
            diferents.append(num)
    diferents.sort()
    return diferents

llista_entrada = [3, 2, 2, 1, 3, 3, 1]
print(nombres_diferents(llista_entrada))	