# 1. In this kata you are required to, given a string, replace every letter
# with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

text = "Once upon a time..."
alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = ''
for letter in text:
    position = alphabet.find(letter.lower()) + 1
    if position > 0:
        res += str(position)
        res += ' '
res = res.strip()
print(res)

# 2. Given an array, find the integer that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
for i in seq:
    if seq.count(i) % 2:
        print(i)
        break

# 3. Write a function, persistence, that takes in a positive parameter num
# and returns its multiplicative persistence, which is the number of times
# you must multiply the digits in num until you reach a single digit.

n = 999
numOfTimes = 0
while n // 10:
    numOfTimes += 1
    current = n
    n = 1
    while current:
        n *= current % 10
        current //= 10
print(numOfTimes)
