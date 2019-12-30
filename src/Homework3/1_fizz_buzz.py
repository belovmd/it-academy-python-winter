for num in range(1, 100):
    fizzbuzz = ''
    if num % 3 == 0:
        fizzbuzz += "Fizz"
    if num % 5 == 0:
        fizzbuzz += "Buzz"
    if fizzbuzz == '':
        fizzbuzz = num
    print(fizzbuzz)
