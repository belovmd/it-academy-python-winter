# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

f = open('pupils.txt')

dct_pupils = {}
for i in range(int(f.readline())):
    for j in range(int(f.readline())):
        dct_pupils[i + 1] = dct_pupils.get(i + 1, set())
        dct_pupils[i + 1].add(f.readline().strip())

big_set = small_set = set()
for el in dct_pupils.values():
    small_set = el if not small_set else small_set & el
    big_set |= el
print('Languages that all pupils know:', small_set)
print('Languages that at least one student knows:', big_set)
