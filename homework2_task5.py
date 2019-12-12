# Посчитать количество строчных (маленьких) и прописных (больших) букв в
# введенной строке. Учитывать только английские буквы.
s = str(input('Введите строку: '))
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = 'abcdefghijklmnopqrstuvwxyz'
n = ''
m = ''
for i in s:
    if i in b:
        n += i
    elif i in c:
        m += i
o = len(n)
p = len(m)
print(' В строке ' + str(o) + ' прописных букв и ' + str(p) +
      ' строчных букв.')
