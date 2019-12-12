num = int(input("Введите N: "))
for nums in range(num):
    print((nums + 1) ** 3)

# Проверка, простое ли введенное число
i = 2
j = 0
while i ** 2 <= num and j != 1:
    if num % i == 0:
        j = 1
    i += 1
if j == 1:
    print(num, " - не простое число")
else:
    print(num, " - простое число")

# Является ли палиндромом
oldNum = num
newNum = 0
while oldNum > 0:
    newNum = newNum * 10 + oldNum % 10
    oldNum //= 10
if num == newNum:
    print(num, " - палиндром")
else:
    print(num, " - не палиндром")

# Первые N чисел Фибоначчи
earlyNum = nextNum = 1
if num < 2:
    quit()
print(earlyNum, end=' ')
print(nextNum, end=' ')
for n in range(2, num):
    temp = earlyNum + nextNum
    earlyNum = nextNum
    nextNum = temp
    print(temp, end=' ')
