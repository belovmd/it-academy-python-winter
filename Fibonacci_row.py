var = int(input('Введите количество элементов ряда: '))
F1 = F2 = 1
if var < 2:
    print(var)
else:
    print(F1, end=' ')
    print(F2, end=' ')
    for i in range(2, var):
        F3 = F1 + F2
        F1 = F2
        F2 = F3
        print(F3, end=' ')
