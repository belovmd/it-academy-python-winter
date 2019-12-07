# 1 - Определить, делится ли число на 17.
num = input('Input a number:\n')
num = int(num)
if num % 17 == 0:
    print('%d is divided by 17.' % num)
else:
    print('%d is not divided by 17.' % num)

# 2 - Определить, является ли введенное число простым.
num = input('Input a number:\n')
num = int(num)
for i in range(2, num - 1):
    if num % i == 0:
        print('%d is not a simple number...' % num)
        exit()
print('%d is a simple number!' % num)

# 3 - Определить, является ли число палиндромом.
num = input('Input a number:\n')
num_length = len(num) // 2
for i in range(0, num_length - 1):
    if num[i] != num[len(num) - 1 - i]:
        print('%s is not a palindrome...' % num)
        exit()
print('%s is a palindrome!' % num)
