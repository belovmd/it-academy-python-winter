"""
5. Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""

my_string = 'aAaZ BBbb aa bbb C bbbAqAz bb b b Aaa ББ вв ггОО Q ЖGж'
print(my_string)
num_big = 0
num_small = 0
for cur_letter in my_string:
    if ('a' <= cur_letter <= 'z') or ('A' <= cur_letter <= 'Z'):
        if cur_letter.islower():
            num_small += 1
        else:
            num_big += 1
print('Прописных (больших) английских букв -', num_big)
print('Строчных (маленьких) английских букв -', num_small)
