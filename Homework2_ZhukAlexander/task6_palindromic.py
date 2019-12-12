# Определяет, является ли введенное число
# палиндромом

num = int(input("Введите N: "))
oldNum = num
newNum = 0
while oldNum > 0:
    newNum = newNum * 10 + oldNum % 10
    oldNum //= 10
if num == newNum:
    print(num, " - палиндром")
else:
    print(num, " - не палиндром")
