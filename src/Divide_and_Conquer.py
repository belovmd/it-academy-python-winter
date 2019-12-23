# Given a mixed array of number and string representations of integers,
# add up the string integers and subtract this from the total
# of the non-string integers. Return as a number.


def div_con(my_list):
    string = 0
    numeral = 0
    for i in my_list:
        if str(i) == i:
            i = int(i)
            string += i
        else:
            numeral += i
    return numeral - string


print(div_con([12, 13, '12', '7']))
