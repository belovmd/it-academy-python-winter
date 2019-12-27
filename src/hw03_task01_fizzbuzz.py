"""
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


for number in range(1, 101):
    strin_pr = ''
    if not number % 3:
        strin_pr += 'Fizz'
    if not number % 5:
        strin_pr += 'Buzz'
    if strin_pr == '':
        strin_pr = number
    print(strin_pr)
