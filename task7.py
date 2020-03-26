# 7. Задание: Даны два натуральных числа.
# Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида

first_num = int(input())
second_num = int(input())
while first_num and second_num:
    if first_num > second_num:
        first_num %= second_num
    else:
        second_num %= first_num
print(first_num + second_num)
