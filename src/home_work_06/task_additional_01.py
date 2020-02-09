def fibonacci_number(fib_number=None):
    if not fib_number:
        fib_number = int(input('Enter number:\n'))

    def fib(number):
        prev_num, curr_num = 0, 1
        for num in range(number):
            yield prev_num
            prev_num, curr_num = curr_num, prev_num + curr_num

    res = list(fib(fib_number))
    return res[-1]


print(fibonacci_number())
print(fibonacci_number(10))
