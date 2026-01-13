from difflib import get_close_matches

def llegir_txt (base_dades: str):
    txt = []
    with open (base_dades) as arxiu_txt:
        for fila in arxiu_txt:
            txt.append(fila.strip())
    return txt


def corregir_text (text: str, diccionari: list):
    paraules_text = text.split(" ")
    text_corregit = ""
    paraules_erronies = {}
    
    for paraula in paraules_text:
        if paraula.lower() in diccionari:
            text_corregit += f"{paraula} "
        else:
            text_corregit += f"*{paraula}* "
            paraules_erronies [paraula] = get_close_matches(paraula, diccionari)
    
    print (text_corregit)
    print ("suggestions:")
    for paraula, suggeriments in paraules_erronies.items():
        print (f"{paraula}: ",end = "")
        for suggeriment in suggeriments:
            print (f"{suggeriment}, ", end = "")
        print ("")
            
def main ():
    diccionari = llegir_txt ("diccionari.txt")
    frase = input ("write a text: ")
    corregir_text (frase, diccionari)

main ()