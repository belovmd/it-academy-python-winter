"""
Даны два натуральных числа. Вычислить их наибольший
общий делитель при помощи алгоритма Евклида

"""

first_num = int(input("Первое число: "))
second_num = int(input("Второе число: "))
while first_num != second_num:          # нахождение НОД вычитанием
    if first_num > second_num:
        first_num -= second_num
    else:
        second_num -= first_num
print(first_num)

first_num = int(input("Первое число: "))
second_num = int(input("Второе число: "))
while first_num != 0 and second_num != 0:       # нахождение НОД делением
    if first_num > second_num:
        first_num %= second_num
    else:
        second_num %= first_num
print(first_num + second_num)
