# 5. Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

string = input('Enter the string: ', )
lower = upper = 0
for i in string:
    if 'a' <= i <= 'z':
        lower += 1
    elif 'A' <= i <= 'Z':
        upper += 1
print("Number of English letters, lower case:", lower, "upper case:", upper)
