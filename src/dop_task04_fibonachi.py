# ряд фибаначи
#  end=' ' в строчку пусть выводит
# вопрос: начинать с 0 как в wiki или с 1 как в школьном учебнике?
num = int(input('Введите к-во чисел: '))
numFib1 = 0
numFib2 = 1
if num >= 2:
    print(numFib1, end=' ')
    print(numFib2, end=' ')
    for i in range(2, num):
        numFib1, numFib2 = numFib2, numFib1 + numFib2
        print(numFib2, end=' ')
else:
    print(numFib1)
    print('ряд - это минимум 2 элемента')
