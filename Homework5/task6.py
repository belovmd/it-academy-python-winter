# 6. Вводится число. найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).

num = int(input('Enter the number: '))
two_expo = 1
divisor = 1
while two_expo < num:
    two_expo = two_expo << 1
    if num % two_expo == 0:
        divisor = two_expo
print(divisor)
