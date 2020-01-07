lst1 = [first + second for first in "ab" for second in "bcd"]
print(lst1)
print(lst1[::2])
lst2 = [first + second for first in "1234" for second in "a"]
print(lst2)
lst2.remove('2a')
print(lst2)
lst3 = lst2.copy()
lst3.append('2a')
print(lst2, lst3)
