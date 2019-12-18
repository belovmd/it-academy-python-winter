"""
1. First task
Multiply two numbers
"""


def mult_two(a, b):
    c = a * b
    return c


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

print('=' * 100)

'''
2. In this mission you should write a function
that introduces a person with the given parameter's attributes.
'''


# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {} and I'm {} years old".format(name, age)


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
    print('Done. Time to Check.')

print('=' * 100)

"""
3. Your mission here is to create a function that gets a tuple
and returns a tuple with 3 elements - the first,
third and second to the last for the given array.
"""


def easy_unpack(elements: tuple) -> tuple:
    (a, b, c) = (elements[0], elements[2], elements[-2])
    return a, b, c


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

print('=' * 100)

"""
You are given an array with positive numbers and a number N.
You should find the N-th power of the element in the array with the index N.
If N is outside of the array, then return -1.
Don't forget that the first element has the index 0.
"""


def index_power(array: list, n: int) -> int:
    if n <= len(array) - 1:
        power = array[n] ** n
    else:
        power = -1
    return power


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    # These "asserts" using only for self-checking
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests!")

print('=' * 100)

"""
5.You are given a positive integer.
Your function should calculate the product of the digits excluding any zeroes.
"""


def checkio(number: int) -> int:
    result = 1
    for i in str(number):
        n = int(i)
        if n:
            result *= n
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests!")
