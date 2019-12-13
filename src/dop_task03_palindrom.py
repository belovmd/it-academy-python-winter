# палиндром
# палиндром - одинаково читающееся в обоих направлениях.
num = int(input('Введите число: '))
tempNum = num
num2 = 0
if num < 0:
    print(num, ' - не палиндром')
else:
    while tempNum > 0:
        num2 = num2 * 10 + tempNum % 10
        tempNum = tempNum // 10
    else:
        if num == num2:
            print(num, ' - палинром')
        else:
            print(num, ' - не палиндром')
