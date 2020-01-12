# Даны два натуральных числа. Вычислите их наибольший
# общий делитель при помощи алгоритма Евклида.

num1 = int(input('First number: '))
num2 = int(input('Second number: '))
if num1 < num2:
    num1, num2 = num2, num1
while num1 % num2:
    num1, num2 = num2, num1 % num2
print('GSD:', num2)
