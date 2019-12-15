"""
Проверить, является ли число простым
"""

n = int(input("Введите число: \n"))  # enter number
c = n  # number 2
while n > 1:
    n -= 1  # division number 2 on number 1 -= 1
    if c % n == 0 and n != 1:
        print("Не простое, а золотое")
        break
    elif n == 1:
        print("Простое")
