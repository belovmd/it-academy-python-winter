"""In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.l"""
## Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
def high_and_low(numbers):
    a = c = ''
    i = b = t = 0
    while i < len(numbers):
        if '0' <= numbers[i] <= '9' or numbers[i] == '-':
            while i < len(numbers):
                if '0' <= numbers[i] <= '9' or numbers[i] == '-':
                    a += numbers[i]
                    i += 1
                else:
                    break
        else:
            None
        t = int(a)
        if t > b and c == '':
            b = t
            c = t
        elif t > b:
            b = t
        elif t < c:
            c = t
        else:
            None
        i += 1
        a = ''
    b = str(b)
    c = str(c)
    numbers = b + ' ' + c
    return numbers
