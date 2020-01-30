"""Создайте декоратор,
который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)"""


def dec(fun):
    count = 0
    my_file = open("snake.txt", "a+")
    my_file.write('1')
    my_file.close()
    my_file = open('snake.txt')
    my_str = my_file.read()
    print(my_str)
    my_file.close()

    for i in my_str:
        count += int(i)
    print('функция вызывалась ', count, ' раз(а)')

    def wrapper():
        return fun()

    return wrapper


@dec
def func():
    pass


func()
