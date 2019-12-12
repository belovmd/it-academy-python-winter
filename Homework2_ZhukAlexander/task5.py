# Считаем количество строчных и прописных букв
# вариант первый

enterString = input("Введите строку (англ. символы): ")
upLet = 0
lowLet = 0
upLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowLetters = 'abcdefghijklmnopqrstuvwxyz'
for letter in enterString:
    if letter in upLetters:
        upLet += 1
    elif letter in lowLetters:
        lowLet += 1
    else:
        continue
print('Строчных букв: ', lowLet)
print('Прописных букв: ', upLet)

# вариант второй
enterString = input("Введите строку (англ. символы): ")
upLet = 0
lowLet = 0
for letter in enterString:
    if 'A' <= letter <= 'Z':
        upLet +=1
    elif 'a' <= letter <= 'z':
        lowLet +=1
    else:
        continue
print('Строчных букв: ', lowLet)
print('Прописных букв: ', upLet)
