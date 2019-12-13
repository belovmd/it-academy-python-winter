"""
Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке.
Учитывать только английские буквы
"""
word = input()

small = 0
big = 0
for i in word:
    if 'a' <= i <= 'z':
        small += 1
    elif 'A' <= i <= 'Z':
        big += 1
print(small)
print(big)
