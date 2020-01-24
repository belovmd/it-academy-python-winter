"""Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько
различных слов содержится в этом тексте.

"""

import re

# Это регулярное срезает пробельные символы и знаки препинания.
data = set(re.findall(r"\w+", input("Введи строку: ").lower()))
print(len(data))
