paraula = input ("Paraula: ")

espais1 = " " * int(((28 - len (paraula)) / 2))
espais2 = ""

if len(paraula) % 2 == 0:
    espais2 = espais1
else:
    espais2 = espais1 + " "

print ("*" * 30)
print ("*" + espais1 + paraula + espais2 + "*")
print ("*" * 30)
