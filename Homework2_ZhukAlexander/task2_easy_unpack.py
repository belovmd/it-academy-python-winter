#  Create a function that gets a tuple
#  and returns a tuple with 3 elements -
#  the first, third and second
#  to the last for the given array.


def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """

    first_elem = elements[0]
    second_elem = elements[2]
    pre_last = elements[-2]
    new_tuple = (first_elem, second_elem, pre_last)
    return new_tuple


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
