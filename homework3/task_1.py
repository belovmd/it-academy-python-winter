# FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
# одновременно кратных и 3 и 5 - FizzBuzz

lst = []
for element in range(1, 100):
    if element % 3 == 0 and element % 5 != 0:
        element = 'Fizz'
        lst.append(element)
    elif element % 5 == 0 and element % 3 != 0:
        element = 'Buzz'
        lst.append(element)
    elif element % 5 == 0 and element % 3 == 0:
        element = 'FizzBuzz'
        lst.append(element)
    else:
        lst.append(element)
print(lst)
