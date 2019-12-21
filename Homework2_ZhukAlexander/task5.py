# Считаем количество строчных и прописных букв
# вариант первый

enter_string = input("Введите строку (англ. символы): ")
up_let = 0
low_let = 0
up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
for letter in enter_string:
    if letter in up_letters:
        up_let += 1
    elif letter in low_letters:
        low_let += 1
    else:
        continue
print('Строчных букв: ', low_let)
print('Прописных букв: ', up_let)

# вариант второй
enter_string = input("Введите строку (англ. символы): ")
upLet = 0
lowLet = 0
for letter in enter_string:
    if 'A' <= letter <= 'Z':
        upLet += 1
    elif 'a' <= letter <= 'z':
        lowLet += 1
    else:
        continue
print('Строчных букв: ', low_let)
print('Прописных букв: ', up_let)

# вариант третий
enter_string = input("Введите строку (англ. символы): ")
upLet = 0
lowLet = 0
for letter in enter_string:
    if letter.isupper():
        upLet += 1
    elif letter.islower():
        lowLet += 1
    else:
        continue
print('Строчных букв: ', low_let)
print('Прописных букв: ', up_let)
