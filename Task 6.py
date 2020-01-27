# Во входной строке записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.
user_input = input().split()
lst_output = []
for i in range(len(user_input)):
    if user_input[i] in lst_output:
        continue
    else:
        lst_output.append(user_input[i])
print(len(lst_output))
