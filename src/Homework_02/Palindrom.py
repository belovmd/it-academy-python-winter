num = int(input('Введите число\n'))
num_length = 1
num_division = num
while num_division // 10 > 0:
    num_length += 1
    num_division //= 10
print('Длина числа', num_length)

num_x = num
for i in range(num_length // 2):
    n1 = num_x // 10 ** (num_length - 1)
    n2 = num_x % 10
    print('Сравниваем крайние цифры', n1, n2)
    num_x = (num_x - n1 * 10 ** (num_length - 1)) // 10
    num_length -= 2
    if n1 != n2:
        print(num, 'не палиндром')
        break
else:
    print(num, 'палиндром')
