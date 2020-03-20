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


def lenguagies():
    pupils = {}
    languges = []
    p = set()
    o = set()

    n = int(input("Enter quantity of pupils: "))
    for pupil in range(1, n + 1):
        quantity_languages = int(input('Enter, how much languages '
                                       'knows ' + str(pupil) + ' pupil: '))
        for i in range(1, quantity_languages + 1):
            i = str(input('His ' + str(i) + ' language is : '))
            languges.append(i)
        pupils[pupil] = {a for a in languges}
        languges.clear()
    print(pupils)

    s = pupils.keys()
    s = len(s)

    for i in range(1, s + 1):
        if i < s:
            p = pupils[i] & pupils[i + 1]
        else:
            p &= pupils[i]

    print('All pupils knows ' + str(len(p)) + ' languages: ')
    for i in p:
        print(i)

    for i in range(1, s + 1):
        o.update(pupils[i])

    print(str(len(o)) + ' languages know least one pupil it is: ')
    for i in o:
        print(i)


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
