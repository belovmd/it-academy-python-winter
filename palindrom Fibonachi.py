userNum = int(input("введите число\n"))

for i in range(1, userNum + 1):
    print(i ** 3)
for a in range(userNum):
    if userNum % (a + 2) == 0 and a != userNum - 2:
        print("не очень-то и простое")
        break
    print("простое")
    break  # я не очень понимаю зачем здесь break

fib0, fib1 = 0, 1  # числа Фибоначчи

for u in range(userNum):
    a = fib0 + fib1
    fib0 = fib1
    fib1 = a
    print(fib1)

leng = len(str(userNum))  # палиндром
if leng != 1:
    for j in range(leng):
        if str(userNum)[j] == str(userNum)[leng - 1 - j]:
            pass
        else:
            print("число не является палиндромом")
            break
        print("число является палиндромом")
        break
else:
    print("число является натуральным")
