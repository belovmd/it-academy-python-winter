"""
Создать декоратор, который хранит результат вызова функции
(за всё время вызовов, не только текущий запуск программы
"""


def result_decor(func):
    def wrapper(*args, **kwargs):
        with open('results_of_func.txt', 'a') as f:
            f.write(func()+'\n')
        return func
    return wrapper


@result_decor
def fibon_num():
    print("Выводит N-e число Фибоначчи")
    num = int(input("Введите N: "))
    early_num = next_num = 1      # т.к. 1й и 2й элементы посл-ти == 1
    for n in range(2, num):
        temp = early_num + next_num
        early_num = next_num
        next_num = temp
    return f"for N={num} Fibonachchi number = " + str(next_num)


fibon_num()
