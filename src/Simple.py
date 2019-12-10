n = int(input("Введите число: \n"))
c = n
while n > 1:
    n -= 1
    if c % n == 0 and n != 1:
        print("Не простое, а золотое")
        break
    elif n == 1:
        print("Простое")
