num = int(input("Input a number:\n"))
(prev, cur) = (0, 1)
for i in range(0, num):
    print(cur, end=" ")
    (prev, cur) = (cur, prev + cur)
