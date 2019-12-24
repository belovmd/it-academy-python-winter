# палиндром
# палиндром - одинаково читающееся в обоих направлениях.
num = int(input('Введите число: '))
temp_num = num
num2 = 0
if num < 0:
    print(num, ' - не палиндром')
else:
    while temp_num:
        num2 = num2 * 10 + temp_num % 10
        temp_num //= 10
    else:
        if num == num2:
            print(num, ' - палинром')
        else:
            print(num, ' - не палиндром')
