n = int(input('Введите целое число\n'))
copy_num = abs(n)
revers_num = 0
while copy_num:
    digit = copy_num % 10
    revers_num = revers_num * 10 + digit
    copy_num = copy_num // 10
if n == revers_num:
    print('Это палиндром!')
elif abs(n) == revers_num:
    print('Это отрицательный :-) палиндром!')
else:
    print('Это не палиндром!')
