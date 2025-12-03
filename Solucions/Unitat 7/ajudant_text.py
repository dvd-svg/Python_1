def canviar_majuscules(text_original: str):
    nou_text = "" 
    
    for caracter in text_original:
        if caracter.isupper():
            nou_text += caracter.lower()
        elif caracter.islower():
            nou_text += caracter.upper()
        else:
            nou_text += caracter
            
    return nou_text

def dividir_meitat(text_original: str):
    meitat = len(text_original) // 2
    text1, text2 = text_original [: meitat] , text_original [meitat :]
    
    return (text1, text2)

def eliminar_caracters_especials(text_original: str):
    caracters_permesos = "àáèéìíòóúùÀÁÈÉÌÍÒÓÙÚabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    nou_text = ""
    
    for caracter in text_original:
        if caracter in caracters_permesos:
            nou_text += caracter
    
    return nou_text
    

if __name__ == '__main__':
    print (canviar_majuscules ("Hola com estàs!"))
    print (dividir_meitat ("Hola com estàs!"))
    print (dividir_meitat ("Hola com estàs"))
    print (eliminar_caracters_especials ("Hola, *com* estàs?"))