"""- Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку)"""
a = int(input("Введите целое положительное число: "))
while (int(a) <= 0):
    a = int(input("Попробуйте еще раз: "))
b = n = m = 0
c = a
## Определяем количество разрядов
while (a // (10 ** n)) != 0:
    n += 1
n -= 1
## Немного магии
while n >= 0:
    ## ( n00000 => 00000m )
    b += (c // (10 ** n)) * (10 ** m)
    c = c % (10 ** n)
    m += 1
    n -= 1
## Сравниваем полученый результат с помощью магии и входное число
if a == b:
    print("Введенное число палиндром")
else:
    print("Введенное число не палиндром")
