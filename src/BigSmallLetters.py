# при помощи ord находим юникод буквы,
# и если юникод меньше 97 - это большие
# если больше - маленькие.
word = input()
small = 0
big = 0
for letter in word:
    if letter.isupper():
        big += 1
    else:
        small += 1
print(big, 'Big')
print(small, 'Small')
