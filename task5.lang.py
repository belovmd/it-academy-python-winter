# 6/ Языки
# Каждый из N школьников некоторой
# школы знает Mi языков. Определите,
# какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

union = set()
all_1 = set()

for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)}
    all_1.update(a)
    if i == 1:
        union.update(a)
    else:
        union &= a
print(len(union))
print('\n'.join(sorted(union)))
print(len(all_1))
# print('\n'.join(sorted(all_1)))
