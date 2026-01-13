def nova_persona(nom_cognom: str, edat: int):
    
    if nom_cognom == "":
        raise ValueError ("El nom és una cadena buida: " + nom_cognom)
    elif len(nom_cognom.split (" "))<2:
        raise ValueError ("El nom i el cognom han de ser 2 paraules separades: " + nom_cognom)
    elif len(nom_cognom)>40:
        raise ValueError ("El nom i cognom són massa llargs: " + nom_cognom)
    
    if edat < 0:
        raise ValueError ("L'edat no pot ser negativa: " + str(edat))
    elif edat > 150:
        raise ValueError ("L'edat no pot ser superior a 150: " + str(edat))
    
    return (nom_cognom, edat)

nova_persona ("Pere Piton", 35)