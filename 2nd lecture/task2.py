import math

a = float(input("1ая сторона ", ))
b = float(input("2ая сторона ", ))
c = float(input("3ья сторона ", ))
p = (a + b + c) / 2
if a + b > c or a + c > b or b + c > a:
    print("s =", math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    print("Это не треугольник")
