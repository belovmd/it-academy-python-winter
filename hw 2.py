x = int(input())

# возведение в куб
for i in range(1, x+1):
    print('{0} в кубе равно {1}'.format(i, i**3))

# простые числа
if x >= 2:
    for i in range(2, x-1):
        if x % i == 0 and x != 2:
            print('Число {0} сложное'.format(x))
            break
    else:
        print('Число {0} простое'.format(x))
else:
    print('Введенное число не является ни простым ни сложным')

# палиндром
lenn = len(str(x))
x = int(x)
iter = lenn//2
second, hlast = x, x
if iter >= 1:
    for j in range(1, iter+1):
        # берем первую/вторую и тд. цифры с начала до середины
        first = second//(10**(lenn-j))
        second = int(((second/(10**(lenn-j)))-first)*(10**(lenn-j)))
        # берем первую/вторую и тд. цифры с конца до середины
        prepredlast = ((hlast/(10**j))-(hlast//(10**j)))*(10**j)
        predlast = round(prepredlast)
        last = int((predlast*10)/(10**j))
        # сравниваем первую и последнюю цифру, вторую и предпоследнюю и тд. если они не равны, то это не палиндром
        if first != last:
            print('Число {0} не палиндром'.format(x))
            break
    if first == last:
        print('Число {0} палиндром'.format(x))
else:
    print('Вы ввели однозначное число, это не палиндром')
# числа Фибоначи
if x > 2:
    f1, f2 = 0, 1
    print(f1, f2, end = " ")
    for i in range (2, x):
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')
else:
    print('Слишком мало чисел для числовой последовательности')
