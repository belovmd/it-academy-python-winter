# Создайте декоратор, который хранит результаты вызовы функции
# (за все время вызовов, не только текущий запуск программы)


def dec(fun):
    num_call = 0
    txt = open("function call.txt", "a+")
    txt.write('1')
    txt.close()
    txt = open('function call.txt')
    line = txt.read()
    txt.close()

    for i in line:
        num_call += int(i)
    print('Функция вызвана {0} раз'.format(num_call))

    def wrapper():
        return fun()

    return wrapper


@dec
def func():
    pass

    func()
