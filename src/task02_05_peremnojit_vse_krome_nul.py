def checkio(number: int) -> int:
    endnumber = 1
    while number > 1:
        tempnumber = number // 10
        if number % 10 != 0:
            endnumber *= number % 10
            number = tempnumber
        else:
            number = tempnumber
    return endnumber


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' "
          "to review your tests and earn cool rewards!")
