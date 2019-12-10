var = int(input('Введите число: '))
z = var
y = 0
i = 0
while z != 0:
    n = int(z % (10 ** (i + 1)))
    num = int(n / (10 ** i))
    z = z - n
    y = y * 10 + num
    i += 1
if var == y:
    print('Данное число является палиндромом')
else:
    print('Данное число не является палиндромом')
