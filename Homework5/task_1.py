# Оформите решение задач из прошлых домашних работ в функции. Напишите
# функцию runner.
# runner_a() – все фукнции вызываются по очереди
# runner_b(‘func_name’) – вызывается только функцию func_name.
# runner_c(‘func’, ‘func1’...) - вызывает все переданные функции


def gen_dct():
    dct = {key: key ** 3 for key in range(1, 21)}
    print(dct)
    return dct


def intersec():
    lst1 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])
    # print(lst1)

    lst2 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])
    # print(lst2)

    print(len(lst1.intersection(lst2)))
    # print(lst1 & lst2)
    return len(lst1.intersection(lst2))


def semetric():
    lst1 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])
    # print(lst1)

    lst2 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])
    # print(lst2)

    print(len(lst1.symmetric_difference(lst2)))
    # print(lst1.symmetric_difference(lst2))
    return len(lst1.symmetric_difference(lst2))


def words():
    new_lst = []
    text = input(str(" Type some text: "))
    lst = text.split()
    for word in lst:
        word.strip()
        new_lst.append(word)
    print(len(new_lst))


def evklid():
    a = int(input("Type first number: "))
    b = int(input("Type second number: "))
    if a < b:
        a, b = b, a
    ost = a % b
    while ost != 0:
        ost = a % b
        a, b, = b, ost
    print(a)


# print(globals())


def runner(*func):
    functions = {fun: path for fun, path in globals().items()
                 if not fun.startswith('_')}
    if not func:
        for i in functions:
            functions[i]()
    else:
        for i in [*func]:
            functions[i]()


# runner()
# runner()
runner('evklid', 'gen_dct', 'semetric')
