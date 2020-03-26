"""Создайте декоратор,
который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)"""


def dec(fun):
    def wrapper():
        count = 0
        my_file = open("snake.txt", "a+")
        my_file.write('1')
        my_file = open('snake.txt')
        my_str = my_file.read()
        my_file.close()
        for i in my_str:
            count += int(i)
        print('функция вызывалась ', count, ' раз(а)')
        return fun
    return wrapper
