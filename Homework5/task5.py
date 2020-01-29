# 5. Написать программу которая находит ближайшую степень двойки
# к введенному числу. 10(8), 20(16), 1(1)

num = int(input('Enter the number: '))
two_expo = 1
while two_expo < num:
    two_expo = two_expo << 1
# Условие для случаев, когда заданное число больше ближайшей степени двух
if two_expo - num < num - (two_expo >> 1):
    print(two_expo)
else:
    print(two_expo >> 1)
