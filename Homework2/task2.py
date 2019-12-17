# 2. https://py.checkio.org
# Say Hi
# В этой миссии вы должны написать функцию,
# которая представит человека по переданным параметрам.
# Входные данные: Два аргумента строка(str) и положительное число(int)
# Output: Строка(str).


def say_hi(name, age):
    age = str(age)
    return "Hi. My name is " + name + " and I'm " + age + " years old"


# https://acmp.ru/index.asp?main=task&id_task=18
#  Факториал
# Требуется вычислить факториал целого числа N.

factorial = 1
N = int(input("Enter an integer for the factorial: "))
for i in range(1, N + 1):
    factorial *= i
print("Factorial=", factorial)

# https://acmp.ru/index.asp?main=task&id_task=384
# Числа Фибоначчи - 3
# Требуется найти наибольший общий делитель двух чисел Фибоначчи.

i = int(input("Enter the indices of the Fibonacci numbers: ", ))
j = int(input("Enter the indices of the Fibonacci numbers: ", ))


def fibo(x):
    num_fibo = 0
    num_fibo_before_prev = 0
    num_fibo_prev = 1
    if x == 1:
        num_fibo = 1
    else:
        for k in range(1, x):
            num_fibo = num_fibo_prev + num_fibo_before_prev
            num_fibo_before_prev = num_fibo_prev
            num_fibo_prev = num_fibo
    return num_fibo


fibo1 = fibo(i)
fibo2 = fibo(j)
print("1st Fibonacci number=", fibo1)
print("2nd Fibonacci number=", fibo2)

while fibo1 != fibo2:
    if fibo1 > fibo2:
        fibo1 = fibo1 - fibo2
    else:
        fibo2 = fibo2 - fibo1

print("GCD=", fibo1)  # greatest common divisor
