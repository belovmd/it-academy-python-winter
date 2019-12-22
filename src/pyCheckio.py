def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
# These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")


# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:

    return "Hi. My name is {} and I'm {} years old".format(name, age)


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "My name is Alex,I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "My name is Frank,I'm 68 years old", "Second"
    print('Done. Time to Check.')


def easy_unpack(elements: tuple) -> tuple:
    
    return (elements[0], elements[2], elements[-2])


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')


def index_power(array, n):
    if len(array) <= n:
        return -1

    else:
        return array[n] ** n


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Click 'Check' to review your tests!")


def checkio(number: int) -> int:
    num = 1
    arr = str(number)
    for x in arr:
        if x != '0':
            num *= int(x)

    return num


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Click 'Check' to review your tests and earn cool rewards!")
