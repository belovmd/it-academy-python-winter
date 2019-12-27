# 1. FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

lst = [str(num) for num in range(1, 101)]
for num in range(len(lst)):
    if int(lst[num]) % 3 == 0 and int(lst[num]) % 5 == 0:
        lst[num] = 'FizzBuzz'
    elif int(lst[num]) % 3 == 0:
        lst[num] = 'Fizz'
    elif int(lst[num]) % 5 == 0:
        lst[num] = 'Buzz'

# Вывод результата по 25 элементов в строке чтобы поместить на экран.
for num_string in range(1, 5):
    print(' '.join([lst[num]
                    for num in range((num_string - 1) * 25,
                                     num_string * 25)]))
