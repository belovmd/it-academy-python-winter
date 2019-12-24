"""1.FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100,
о вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
 а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""
for numeric in range(101):
    if numeric % 3 == 0 and numeric % 5 == 0:
        print('FizzBuzz')
    elif numeric % 5 == 0:
        print('Buzz')
    elif numeric % 3 == 0:
        print('Fizz')
    else:
        print(numeric)
