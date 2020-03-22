# Написать программу которая находит ближайшую
# степень двойки к введенному числу. 10(8), 20(16), 1(1)
user_input = int(input())
one = 1
while one <= user_input:
    one <<= 1
if abs(one - user_input) >= abs((one >> 1) - user_input):
    one = one >> 1
    print(one)
else:
    print(one)
