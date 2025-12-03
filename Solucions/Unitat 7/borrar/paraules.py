def primera_paraula(meu_text: str):
    parts = meu_text.split(" ")
    return parts[0]

def darrera_paraula(meu_text: str):
    parts = meu_text.split(" ")
    return parts[-1]

def nombre_paraules(meu_text: str):
    parts = meu_text.split(" ")
    return len(parts)