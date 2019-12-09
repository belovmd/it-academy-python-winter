# --------1st variant-----------
line = input()
p = len(line)

for i in range(p // 2):
    if line[i] != line[-1 - i]:
        print('no')
        quit()

print('yes')

# -------2nd variant------------

p = line[:: - 1]

if line == p:
    print('yes')
else:
    print('no')

# ---------------------------------------------------------------------

n = int(input('Num: '))
a = 0
b = 1

for i in range(n):
    f = a + b
    a = b
    b = f
    print(f)
