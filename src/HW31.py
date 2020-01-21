# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
for num in range(1, 101):
    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("buzz")
    elif num % 5 == 0:
        print("fizz")
    else:
        print(num)
