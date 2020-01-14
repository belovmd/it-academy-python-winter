# Даны два списка чисел.
# Посчитайте, сколько различных
# чисел входит только в один из этих списков

a = set(input().split())
b = set(input().split())
count = 0
d = []
for i in a:
    if i not in b:
        d.append(i)
print(len(d))
