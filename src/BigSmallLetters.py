# Посчитать количество строчных (маленьких) и прописных 
# (больших) букв в введенной строке. 
# Учитывать только английские буквы.
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
