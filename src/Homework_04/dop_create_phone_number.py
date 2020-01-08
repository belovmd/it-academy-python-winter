"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
Example:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] => "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""


#  мое решение
def create_phone_number_v1(num_list):
    num = ''.join(str(elem) for elem in num_list)
    return '(' + str(num[0:3]) + ') ' + str(num[3:6]) + '-' + str(num[6:])


#  нашел интересное решение, но пишут, что это не самое читаемое
def create_phone_number_v2(num_list):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*num_list)


print(create_phone_number_v1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number_v1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number_v1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number_v1([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number_v1([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
