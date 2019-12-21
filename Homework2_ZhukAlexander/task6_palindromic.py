# Определяет, является ли введенное число
# палиндромом

num = int(input("Введите N: "))
old_num = num
new_num = 0
while old_num > 0:
    newNum = new_num * 10 + old_num % 10
    old_num //= 10
if num == new_num:
    print(num, " - палиндром")
else:
    print(num, " - не палиндром")
