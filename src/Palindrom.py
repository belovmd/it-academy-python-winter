"""
Проверьте, является ли число палиндромом
"""

number = int(input("Введите число: "))
number_1 = number
number_2 = 0
while number_1:
    number_2 = number_2 * 10 + number_1 % 10
    number_1 = number_1 // 10
if number == number_2:
    print("Палиндром")
else:
    print("Не палиндром")
