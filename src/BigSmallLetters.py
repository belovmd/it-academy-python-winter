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
