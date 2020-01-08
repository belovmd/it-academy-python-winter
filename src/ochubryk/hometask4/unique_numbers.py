# Даны два списка чисел. Посчитайте, сколько
# чисел входит только в один из этих списков

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 3, 4, 5, 15, 16, 7]

# print(len(set.difference(set(a), set(b))))
print('Числа, уникальные'
      ' для списка а: ' + str(set.difference(set(a), set(b))))
print('Количество чисел, уникальных'
      ' для списка а: ' + str(len(set.difference(set(a), set(b)))))

print('Числа, уникальные'
      ' для списка b: ' + str(set.difference(set(b), set(a))))
print('Количество чисел, уникальных'
      ' для списка b: ' + str(len(set.difference(set(b), set(a)))))

print('Множество из элементов, встречающихся'
      ' в одном множестве, но не встречающиеся'
      ' в обоих: ' + str(set.symmetric_difference(set(a), set(b))))
print('Количество элементов, встречающихся'
      ' в одном множестве, но не встречающиеся'
      ' в обоих: ' + str(len(set.symmetric_difference(set(a),
                                                      set(b)))))
