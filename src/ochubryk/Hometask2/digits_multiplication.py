# exercise from https://py.checkio.org/
# You are given a positive integer.
# Your function should calculate
# the product of the digits excluding any zeroes.


def checkio(number: int) -> int:
    numbers = str(number)
    numbers = [int(number) for number in numbers if int(number) != 0]

    if len(numbers) >= 2:
        for number in range(len(numbers) - 1):
            result = numbers[number] * numbers[number + 1]
            numbers[number] = numbers[number + 1]
            numbers[number + 1] = result
    if len(numbers) == 1:
        result = numbers[0]

    return int(result)


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
