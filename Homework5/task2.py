# 2. Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)


def data_to_file(func):
    def wrapper():
        with open('file.txt', 'a') as f:
            f.write(func() + '\n')
    return wrapper


# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида
@data_to_file
def gcd():
    number1 = int(input('Enter 1st natural number: '))
    number2 = int(input('Enter 2nd natural number: '))
    data = str(number1) + ' ' + str(number2)   # Для записи в файл
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    print('GCD =', number1)  # greatest common divisor
    data = data + ' GCD = ' + str(number1)
    return data


gcd()
