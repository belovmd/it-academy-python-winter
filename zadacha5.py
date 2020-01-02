# Дан список.
# Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
user = input().split()
uniq = []
for i in range(len(user)):
    if user[i] not in uniq:
        uniq.append(user[i])
print(uniq)
