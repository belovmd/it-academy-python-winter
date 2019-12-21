# Найти самое длинное слово в предложении

import string
enter_string = input("Предложение: ")
func = str.maketrans(dict.fromkeys(string.punctuation))
new_string = enter_string.translate(func)
word_list = new_string.split()
id_long = 0
for i in range(1, len(word_list)):
    if len(word_list[id_long]) < len(word_list[i]):
        id_long = i
print(word_list[id_long])
