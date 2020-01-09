"""
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько различных
слов содержится в этом тексте.

"""

import string
new_str = input("Текст (может быть со знаками): ")
func = str.maketrans(dict.fromkeys(string.punctuation))
clean_str = new_str.translate(func)
words_set = set(clean_str.split())
print(len(words_set))
