from math import sqrt


a = int(input ("Valor de a: "))
b = int(input ("Valor de b: "))
c = int(input ("Valor de c: "))


arrel1 = (-b + sqrt(b*b-4*a*c))/(2*a)
arrel2 = (-b - sqrt(b*b-4*a*c))/(2*a)

print (f"Les arrels són {arrel1} i {arrel2}")
