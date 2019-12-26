# Печатает цифры от 1 до 100
# вместо кратных 3 пишет FIzz
# вместо кратных 5 пишет Buzz
# вместо одновременно кратных 3 и 5 пишет
# FizzBuzz

for num in range(1, 101):
    if not num % 3 and not num % 5:
        print('FizzBuzz')
    elif not num % 3:
        print('Fizz')
    elif not num % 5:
        print('Buzz')
    else:
        print(num)
