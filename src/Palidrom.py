# тут каждый проход цикла удаляется последняя цифра числа a и в
# b суммируется новое число и при этом b умножается на 10
# получаем число наоборот, и сравниваем с
# x который равняется первоначальному числу a
a = int(input('Введите число '))
x = a
b = 0
while a > 0:
    c = a % 10
    a = a // 10
    b = b * 10
    b = c + b
if b == x:
    print('Является палидромом')
else:
    print('Не является палидромом')
