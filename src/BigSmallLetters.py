# при помощи ord находим юникод буквы,
# и если юникод меньше 97 - это большие
# если больше - маленькие.
a = input()
small = 0
big = 0
for i in a:
    if ord(i) >= 97:
        small += 1
    else:
        big += 1
print(big, 'Big')
print(small, 'Small')
