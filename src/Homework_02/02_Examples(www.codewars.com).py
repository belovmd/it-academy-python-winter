"""
1. If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Finish the solution so that it returns
the sum of all the multiples of 3 or 5 below the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    num_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            num_sum += i
    return num_sum


"""
2. Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function
811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    my_string = str(num)
    res_num = ''
    for i in range(len(my_string)):
        x = int(my_string[i]) ** 2
        res_num += str(x)
    return int(res_num)


"""
3. An isogram is a word that has no repeating letters,
consecutive or non-consecutive.
Implement a function that determines
whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):
    my_low_string = string.lower()
    my_new_string = ''
    for i in range(len(my_low_string)):
        if my_new_string.find(my_low_string[i]) == -1:
            my_new_string += my_low_string[i]
    if my_low_string == my_new_string:
        return True
    else:
        return False


"""
4. ATM machines allow 4 or 6 digit PIN codes
and PIN codes can't contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
"""


def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False


"""
5. You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
"""


def get_middle(s):
    if len(s) % 2 == 0:
        mid_string = s[(len(s) / 2) - 1] + s[(len(s) / 2)]
    else:
        mid_string = s[(len(s) // 2)]
    return mid_string
