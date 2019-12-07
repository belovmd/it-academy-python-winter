num = int(input("Input a number:\n"))
currentNum = num
capacity = 0
while currentNum % 10:
    capacity += 1
    currentNum //= 10
currentNum = num
for i in range(0, capacity // 2):
    firstNumber = currentNum // 10 ** (capacity - 1)
    lastNumber = currentNum % 10
    currentNum = (currentNum - firstNumber * 10 ** (capacity - 1)) // 10
    capacity -= 2

    if firstNumber != lastNumber:
        print("%d is not a palindrome" % num)
        break
else:
    print("%d is a palindrome!" % num)
