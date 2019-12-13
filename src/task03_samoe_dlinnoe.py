my_string = '1 22 333 4444 55555 55555, 333. 666666.....  333'
my_string1 = my_string.replace(",", " ")
my_string1 = my_string1.replace(".", " ")
print(my_string1)
my_string2 = my_string1.split()
max_string_count = 0
max_string = ''
print(my_string2)
for i in my_string2:
    if max_string_count < len(i):
        max_string_count = len(i)
        max_string = i
print('маХ длинна - ', max_string_count, 'слово - ', max_string)
