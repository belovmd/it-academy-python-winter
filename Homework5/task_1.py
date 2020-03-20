def gen_dct():
    dct = {key: key ** 3 for key in range(1, 21)}
    print(dct)
    return dct


def intersec():
    lst1 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])

    lst2 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])

    print(len(lst1.intersection(lst2)))
    return len(lst1.intersection(lst2))


def semetric():
    lst1 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])

    lst2 = set([i for i in
                (input('Please, enter the list of numbers '
                       'through space: ')).split()])

    print(len(lst1.symmetric_difference(lst2)))
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


def runner(*func):
    functions = {fun: path for fun, path in globals().items()
                 if not fun.startswith('_')}
    if not func:
        for i in functions:
            if callable(functions[i]):
                functions[i]()
    else:
        for i in [*func]:
            if callable(functions[i]):
                functions[i]()


# runner()
runner('evklid', 'gen_dct', 'semetric')
