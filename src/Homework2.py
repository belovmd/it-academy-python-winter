a = input('Some string: ')

# --------Task 1---------------

b = 0

for p in a.split():
    f = p.strip(",'.'-'!'?")  # this punctuations marks for example
    c = len(f)
    if c >= b:
        b = c
        n = f

print('Symbols: ', b, ' word: ', n)

# ----------Task 3 1st variant-------------

price = float(input('Price (for example 1.50): '))
sub = float(input('How many: '))

bill = price * sub
print('%.2f' % bill)

# -----------2nd variant--------------

M = int(input('Rub: '))
N = int(input('Coin: '))
L = int(input('How many: '))

rub = M * L
coin = N * L

while coin >= 100:
    rub += 1
    coin -= 100

print('Bill: ', rub, ' rub ', coin, ' coins')

# ---------Task 5-------------

small = 0
big = 0

for i in a:
    if 'a' <= i <= 'z':
        small += 1
    else:
        if 'A' <= i <= 'Z':
            big += 1

print('Small letter: ', small)
print('Big latter: ', big)

# ----------Task 4-----------

str = ''

for p in a.split():
    f = p.strip(",'.'-'!'?")  # this punctuations marks for example
    for q in f:
        if q not in str:
            str += q

print(str)
