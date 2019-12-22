number = int(input("Please, enter a number: "))
new_number = number
res = 0
i = 0

while new_number != 0:
    n = int(new_number % (10 ** (i + 1)))
    num = int(n / (10 ** i))
    new_number = new_number - n
    res = res * 10 + num
    i += 1

if number == res:
    print("It's palindrome")
else:
    print("It's not a palindrome")
