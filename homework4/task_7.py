# Оглянемся назад
# Даны два натуральных числа. Вычислите их наибольший общий
# делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
a = int(input("Type first number: "))
b = int(input("Type second number: "))
if a < b:
    a, b = b, a
ost = a % b
while ost != 0:
    ost = a % b
    a, b, = b, ost
print(a)
