stroka = str(input('введите строку:'))


# stroka1 = stroka.replace(' ', '') - можно заменить на разделить/склеить
stroka1 = ''.join(stroka.split())
stroka2 = stroka1[0]
for i in stroka1:
    for j in stroka2:
        if i == j:
            break
    else:
        stroka2 += i
print(stroka2)
