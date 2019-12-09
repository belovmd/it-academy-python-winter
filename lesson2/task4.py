a = int(input("сторона а:"))
b = int(input("сторона b:"))
c = int(input("сторона c:"))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c)/2
    s = (p*(p - a)*(p - b)*(p - c))*0.5
    print(s)
else:
    print("неверные данные ")
