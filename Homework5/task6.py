# 6. Вводится число. найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).

num = abs(int(input('Enter the number: ')))
# модуль числа - для первого варианта решения
# two_expo = 1
# divisor = 1
# while two_expo < num:
#     two_expo = two_expo << 1
#     if num % two_expo == 0:
#         divisor = two_expo
# print(divisor)

two_expo = 1
if num != 0:
    while num & two_expo == 0:
        two_expo = two_expo << 1
print(two_expo)
