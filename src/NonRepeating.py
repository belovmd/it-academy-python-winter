# суммируем в новую переменную каждую новую
# букву. Пробелы сразу заменяем
a = input()
c = ''
a = a.replace(' ', '')
for i in a:
    if i not in c:
        c += i
print(c)
