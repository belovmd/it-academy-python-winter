# prime number
var = int(input("Введите число. var="))
if var < 2:
    print("Необходимо ввести число 2 или больше")
else:
    i = 2
    while i <= var**0.5:
        if var % i == 0:
            print(var, "-составное число")
            break
        i += 1
    else:
        print(var, "-простое число")
for i in range(var):
    p = i + 1
    print(p, '**3=', p ** 3)
# task_2 Palindrom
x = int(input("Введите натуральное число x="))
y = x
z = 0
while y > 0:
    z = z * 10 + y % 10
    y = y // 10
if z == x:
    print(x, "является палиндромом")
else:
    print(x, "не является палиндромом")
# task_3 Fibonacci numbers
n = int(input("Введите количество первых чисел из ряда Фибоначчи. n="))
fib1 = 1
fib2 = 1
fib12 = 0
if n == 1:
    print(fib1)
elif n == 2:
    print(fib1)
    print(fib2)
else:
    print(fib1)
    print(fib2)
    for i in range(n - 2):
        fib12 = fib1 + fib2
        fib1 = fib2
        fib2 = fib12
        print(fib2)
