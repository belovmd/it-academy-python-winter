"""
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

my_string = 'aaa \n\nbbb\n aaa   cc  vvv\nbbb      ddd'
my_new_string = my_string[:]
while my_new_string.find('  ') != -1 or my_new_string.find('\n') != -1:
    my_new_string = my_new_string.replace('\n', ' ')
    my_new_string = my_new_string.replace('  ', ' ')
print('Кол-во разных слов', len(set(my_new_string.split())))
