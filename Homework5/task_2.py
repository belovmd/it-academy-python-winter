# Создайте декоратор, который хранит результаты вызовы функции
# (за все время вызовов, не только текущий запуск программы)


def dec(func):
    s = []
    def wrapper(*args):
        nonlocal s
        s.append(func(*args))
        print(s)
        return func
    return wrapper

@dec
def summator(a, b):
    return a + b

summator(1, 2)
summator(2, 2)
summator(2, 5)
