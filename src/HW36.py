lst = [1, 2, 3, 0, 4, 0, 5, 0, 6, 0, 7]
for element in lst:
    lst.remove(0)
    lst.append(0)
print(lst)
