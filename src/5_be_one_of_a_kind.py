# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке, в котором
# они встречаются в списке.
lst = [int(smth) for smth in input().split()]
for i in range(len(lst)):
    for ch in range(len(lst)):
        if i != ch and lst[i] == lst[ch]:
            break
    else:
        print(lst[i], end=' ')
