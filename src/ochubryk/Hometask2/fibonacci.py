n = int(input())
f1 = f2 = 1

if n < 2:
    print(n)
else:
    print(f1, end=' ')
    print(f2, end=' ')
    for i in range(2, n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f3, end=' ')
