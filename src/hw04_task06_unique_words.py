"""
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца
строки. Определите, сколько различных слов содержится в этом тексте.
"""

import re

stroka01 = ("Lorem Ipsum is simply dummy text of the "
            "printing and typesetting industry. "
            "Lorem Ipsum has been the industry's "
            "standard dummy text ever since the 1500s, "
            "when an unknown printer took a galley of "
            "type and scrambled it to make a type specimen book.")

stroka02 = set(re.split(r'\W+', stroka01))
print(stroka01)
print(len(stroka02), 'уникальных слов(а)')
