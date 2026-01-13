farenheit = int(input("Introdueix una temperatura (F):"))
celsius = (farenheit - 32) * (5/9)

print (f"{farenheit} graus Fahrenheit equivalen a {celsius} graus Celsius")

if celsius < 0:
    print("Brr! Fa fred aquí!")