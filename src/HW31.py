# fizzbuzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("buzz")
    elif num % 5 == 0:
        print("fizz")
    else:
        print(num)
