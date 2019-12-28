# You are given an array of integers. You should find the sum
# of the integers with even indexes (0th, 2nd, 4th...).
# Then multiply this summed number and the final element of
# the array together. Don't forget that the first element has an index of 0.
# For an empty array, the result will always be 0 (zero).


def checkio(array):
    if not array:
        return 0
    else:
        even_lst = array[::2]
        result = sum(even_lst) * array[-1]
        return result


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
