from datetime import datetime

def es_valid (identificacio: str):
    dia = identificacio [:2]
    mes = identificacio [2:4]
    digits_any = identificacio [4:6]
    segle = identificacio [6]
    
    if segle == "+":
        any_ = int("18" + digits_any)
    elif segle == "-":
        any_ = int("19" + digits_any)
    elif segle == "A":
        any_ = int("20" + digits_any)
    else:
        return False
        
    id_personal = identificacio [7:10]
    control = identificacio [10]
    
    try:
        data = datetime (any_, int(mes), int(dia))
    except:
        return False
    
    possible_control = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    control_teoric = possible_control [int (str(dia) + str(mes) + digits_any + id_personal) % 31]
    
    if control_teoric != control:
        return False
    
    return True
    
print (es_valid ("230827-906F"))
print (es_valid ("120488+246P"))
print (es_valid ("310823A9877"))
    