"""
5. Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""

my_string = 'aAaZ BBbb aa bbb C bbbAqAz bb b b Aaa ББ вв ггОО Q ЖGж'
print(my_string)
num_big = 0
num_small = 0
for i in range(len(my_string)):
    cur_letter = my_string[i]
    cur_ind = ord(cur_letter)
    if (65 <= cur_ind <= 90) or (97 <= cur_ind <= 122):
        if cur_letter == my_string[i].lower():
            num_small += 1
        else:
            num_big += 1
print('Прописных (больших) английских букв -', num_big)
print('Строчных (маленьких) английских букв -', num_small)
