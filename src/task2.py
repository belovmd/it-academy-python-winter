from string import Template
#  Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://py.checkio.org/ , https://www.codewars.com,   https://www.hackerrank.com/, https://acmp.ru
# И решите 1-5 задач уровня Elementary или любых других.

# mission1 on py.checkio.org


def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

# mission2 on py.checkio.org


def easy_unpack(elements):
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

# mission3 on py.checkio.org


def say_hi(name, age):
    """
        Hi!
    """
    t = Template("Hi. My name is $name and I'm $age years old")
    return t.substitute(name=name, age=age)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
