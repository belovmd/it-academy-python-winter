"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно
один раз разломить по прямой на две части.
1.	Определите, можно ли таким образом отломить от шоколадки ровно k долек.
2.	Определите, можно ли отломить от шоколадки ровно k одиночных долек
3.	Определите, можно ли отломить от шоколадки ровно k одиночных долек с
помощью s разломов.

Ниже решение только третей задачи
Принцип решения таков. Если стороны у шоколада равны, то ломаем с одной
стороны, чтобы получилась полосочка размером 1*х, затем отламываем по
одинарной дольке. При отсутсвии долек в полосочке переходим к оставшейся части
шоколадки. При количестве необходимых долек равным 1, остатке полосочки 2
и большом количестве надломов пытаемся отломать от следующей полосочки.
При отличии в размере сторон 3 и 4, например, проводим проверку по каждой
грани.
"""
m = int(input("Введите грань м: "))
n = int(input("Введите грань н: "))
k = int(input("Введите количество долек: "))
s = int(input("Введите количество надломов: "))
#  блок 1 (грани равны), ввел больше временных мало ли пригодились бы :)
count1, newm1, newm11, newn1, newn11 = 0, m, m, n, n
newk1, newk11, news1, news11 = k, k, s, s
# блок 2 (грани не равны)
count2, newm2, newm22, newn2, newn22 = 0, m, m, n, n
newk2, newk22, news2, news22 = k, k, s, s
while news1 and newk1:  # check the first side m
    while newm1 and news1 and newk1:
        # Если верхняя грань есть, то продолжаем счет, аналогично надломы,
        # дольки
        # Ломаем до тех пор, пока не закончатся дольки. А ниже проводим
        # проверку
        # хватит ли дольковой площади шоколада для остальных надломов.
        if newm1 > 1:
            newm1 -= 1
            newn1 = n
            news1 -= 1
            while newn1 and news1 and newk1:
                if newn1 > 2:
                    newn1 -= 1
                    count1 += 1
                    newk1 -= 1
                elif newn1 == 2 and newk1 == 1 and news1 >= 2:
                    newn11, newn1 = newn1, 0
                    continue
                # Если в полосочке осталось две одинарные дольки, а нам нужна
                # всего одна и у нас
                # всего один надлом, то и разломить двойную на 1 одинарную не
                # получится
                else:
                    newn11, newn1 = newn1, 0
                    count1 += 2
                    newk1 -= 2
                news1 -= 1
        else:
            newm1 -= 1
            newn1 = n
            while newn1 and news1 and newk1:
                if newn1 > 2:
                    newn1 -= 1
                    count1 += 1
                    newk1 -= 1
                elif newn1 == 2 and newk1 == 1 and news1 >= 2:
                    newn11, newn1 = newn1, 0
                    continue
                else:
                    newn11, newn1 = newn1, 0
                    count1 += 2
                    newk1 -= 2
                news1 -= 1
if m != n:
    while news2 and newk2:  # check the second side n
        while newn2 and news2 and newk2:
            if newn2 > 1:
                newn2 -= 1
                newm2 = m
                news2 -= 1
                while newm2 and news2 and newk2:
                    if newm2 > 2:
                        newm2 -= 1
                        count2 += 1
                        newk2 -= 1
                    elif newm2 == 2 and newk2 == 1 and news2 >= 2:
                        newm22, newm2 = newm2, 0
                        continue
                    else:
                        newm22, newm2 = newm2, 0
                        count2 += 2
                        newk2 -= 2
                    news2 -= 1
            else:
                newn2 -= 1
                newm2 = m
                while newm2 and news2 and newk2:
                    if newm2 > 2:
                        newm2 -= 1
                        count2 += 1
                        newk2 -= 1
                    elif newm2 == 2 and newk2 == 1 and news2 >= 2:
                        newm22, newm2 = newm2, 0
                        continue
                    else:
                        newm22, newm2 = newm2, 0
                        count2 += 2
                        newk2 -= 2
                    news2 -= 1
# Сравниваем отломанные дольки по каждой грани с искомым количеством долек
if k != count1 and k != count2 and k != 1 or n == 0 or m == 0:
    print("Nelzya1")
elif k == count1 and news1 == 0 or k == count2 and news2 == 0 or k == 1:
    print("Mojno1")
elif k == count1 and (n * newm1) % 2 == 0:
    # Далее идет проверка остатка дольковой площади на возможность разломать
    # на
    # двойные дольки. Т.к. двойные - это не одинарные и являются наименьшими
    # возможными, то и проверка будет по ним. Не забывая, что (newn1 - 2) // 2
    # это остаток полосочки, если он не 2 то даст нам дополнительные надломы
    # -2 т.к. целочисленное деление от 2 даст 0, и от тройки также 0
    if (n * newm1 / 2 - 1 + (newn1 - 2) // 2) >= news1:  # -1 это количество
        # надломов меньше на 1 количества долек
        print("Mojno2")
        print(n * newm1)
        print(newn1)
        print(news1)
    else:
        print("Nelzya2")
        print(n * newm1)
        print(newn1)
        print(news1)
elif k == count2 and (m * newn2) % 2 == 0:
    if (m * newn2 / 2 - 1 + (newm2 - 2) // 2) >= news2:  # -1 это
        # количество надломов меньше на 1 количества долек
        print("Mojno3")
    else:
        print("Nelzya3")
elif k == count1 and (n * newm1 - 1) % 2 == 0:  # нечетные
    if (n * newm1 / 2 - 1 + (newn1 - 2) // 2) >= news1:  # -1 это
        # количество надломов меньше на 1 количества долек
        print("Mojno4")
    else:
        print("Nelzya4")
elif k == count2 and (m * newn2 - 1) % 2 == 0:  # нечетные
    if (m * newn2 / 2 - 1 + (newm2 - 2) // 2) >= news2:  # -1 это количество
        # надломов меньше
        # на 1 количества долек
        print("Mojno5")
    else:
        print("Nelzya5")
else:
    print("Nelzya6")
