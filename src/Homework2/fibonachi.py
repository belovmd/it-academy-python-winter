"""- Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""
## первое значение последовательности 0.
n = int(input("Введите длинну последовательности: "))
while (n <= 0):
    print("Число должно быть положительным")
    n = int(input("Введите длинну последовательности: "))
a, b, = 0, 1,
for i in range(n - 1):
    a, b = b, (a + b)
print(a)
