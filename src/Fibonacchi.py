a = int(input("Введите число более 0: \n"))
b = int(0)
c = int(1)
while a == 0:
    a = int(input("Введите число более 0: \n"))
if a == 1:
    print(b)
elif a == 2:
    print(b, c)
else:
    print(b, end=' ')
    print(c, end=' ')
    for i in range(2, a):
        d = b + c
        b = c
        c = d
        print(d, end=" ")
