# Числа Фибоначи
a = int(input('Введите число '))
b = 0
c = 0
x = 0
for i in range(a + 1):
    if i == 0 or i == 1:
        b = i
        c = c + b
        print(i)
    else:
        b = x
        c = c + b
        x = c - b
        print(c)
