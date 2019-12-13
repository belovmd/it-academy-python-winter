# exercise from https://py.checkio.org/
# You are given an array with positive numbers and a number N.
# You should find the N-th power of the element in the array with the index N.
# If N is outside of the array, then return -1.


def index_power(array: list, n: int) -> int:
    if n > len(array) - 1:
        result = -1
    else:
        result = array[n] ** n

    return result


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
