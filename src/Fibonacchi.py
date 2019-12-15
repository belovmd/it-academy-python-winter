"""
Выведите первые n чисел Фибоначчи, (используйте временные переменные для
хранения прошлых значений и цикл for)
"""

qun = int(input("Введите число более 0: \n"))  # количество элементов ряда
number1 = int(0)  # 1 элемент ряда
number2 = int(1)  # 2 элемент ряда
while qun == 0:  # решение нулевого количества ряда
    qun = int(input("Введите число более 0: \n"))
if qun == 1:  # один элемент в ряде
    print(number1)
elif qun == 2:  # два элемент в ряде
    print(number1, number2)
else:  # более двух
    print(number1, end=' ')
    print(number2, end=' ')
    for i in range(2, qun):
        time = number1 + number2
        number1 = number2
        number2 = time
        print(time, end=" ")
