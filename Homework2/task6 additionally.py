# -Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится

n = int(input("Enter the index of the Fibonacci number: ", ))
num_fibo = 0
num_fibo_before_prev = 0
num_fibo_prev = 1
if n == 1:
    num_fibo = 1
else:
    for k in range(1, n):
        num_fibo = num_fibo_prev + num_fibo_before_prev
        num_fibo_before_prev = num_fibo_prev
        num_fibo_prev = num_fibo
print(num_fibo)
