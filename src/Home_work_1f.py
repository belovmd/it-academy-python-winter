def median(pool1):
    """Statistical median to demonstrate doctest.
    >>> median([1, 8, 8, 7, 9, 2, 4, 5, 8])
    6 #change to 7 in order
    to pass the test"""
    copy1 = sorted(pool1)
    size1 = len(copy1)
    if size1 % 2 == 1:
        return copy1[int((size1 - 1) / 2)]
    else:
        return (copy1[int(size1 / 2 - 1)] +
                copy1[int(size1 / 2)]) / 2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
