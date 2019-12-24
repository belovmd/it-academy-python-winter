"""
Проверить, является ли число простым
"""

number = int(input("Введите число: \n"))  # enter number
end = number // 2 + 1
for i in range(2, end):
    if number % i == 0:
        print("Составное")
        break
else:
    print("Простое")
