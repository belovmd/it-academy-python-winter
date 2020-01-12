# FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел
# кратный 5 пишет Buzz, а вместо чисел одновременно
# кратных и 3 и 5 - FizzBuzz

line_count = 0
for i in range(1, 101):
    current = ''
    if i % 3 == 0:
        current = 'Fizz'
    if i % 5 == 0:
        current += 'Buzz'
    if current == '':
        current = i
    print(current, end=' ')
    line_count += 1
    if line_count == 20:
        line_count = 0
        print('\t')
