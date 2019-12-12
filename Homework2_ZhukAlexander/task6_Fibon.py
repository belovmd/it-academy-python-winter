# Выводит N-ое число Фибоначчи

num = int(input("Введите N: "))
earlyNum = nextNum = 1      # т.к. 1й и 2й элементы посл-ти == 1
for n in range(2, num):
    temp = earlyNum + nextNum
    earlyNum = nextNum
    nextNum = temp
print(nextNum)
