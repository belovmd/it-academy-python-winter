# 1. FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

lst = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        lst.append('FizzBuzz')
    elif num % 3 == 0:
        lst.append('Fizz')
    elif num % 5 == 0:
        lst.append('Buzz')
    else:
        lst.append(str(num))

# Вывод результата по 25 элементов в строке чтобы поместить на экран.
for num_string in range(1, 5):
    print(' '.join([lst[num]
                    for num in range((num_string - 1) * 25,
                                     num_string * 25)]))
