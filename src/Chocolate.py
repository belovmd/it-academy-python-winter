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
top = int(input("Введите грань м: "))  # m
left = int(input("Введите грань н: "))  # n
piece = int(input("Введите количество долек: "))  # k
broke = int(input("Введите количество надломов: "))  # s cant use break :((
#  блок 1 (грани равны)
count_top, new_top, new_left, new_piece, new_broke = 0, top, left, piece, broke
# блок 2 (грани не равны)
count_left, new_top_2, new_left_2 = 0, top, left
new_piece_2, news_broke_2 = piece, broke
while new_broke and new_piece:  # check the first side m
    while new_top and new_broke and new_piece:
        # Если верхняя грань есть, то продолжаем счет, аналогично надломы,
        # дольки. Ломаем до тех пор, пока не закончатся дольки. А ниже проводим
        # проверку хватит ли дольковой площади шоколада для остальных надломов.
        if new_top > 1:
            new_top -= 1
            new_left = left
            new_broke -= 1
            while new_left and new_broke and new_piece:
                if new_left > 2:
                    new_left -= 1
                    count_top += 1
                    new_piece -= 1
                elif new_left == 2 and new_piece == 1 and new_broke >= 2:
                    new_left = 0
                    continue
                # Если в полосочке осталось две одинарные дольки, а нам нужна
                # всего одна и у нас
                # всего один надлом, то и разломить двойную на 1 одинарную не
                # получится
                else:
                    new_left = 0
                    count_top += 2
                    new_piece -= 2
                new_broke -= 1
        else:
            new_top -= 1
            new_left = left
            while new_left and new_broke and new_piece:
                if new_left > 2:
                    new_left -= 1
                    count_top += 1
                    new_piece -= 1
                elif new_left == 2 and new_piece == 1 and new_broke >= 2:
                    new_left = 0
                    continue
                else:
                    new_left = 0
                    count_top += 2
                    new_piece -= 2
                new_broke -= 1
if top != left:
    while news_broke_2 and new_piece_2:  # check the second side n
        while new_left_2 and news_broke_2 and new_piece_2:
            if new_left_2 > 1:
                new_left_2 -= 1
                new_top_2 = top
                news_broke_2 -= 1
                while new_top_2 and news_broke_2 and new_piece_2:
                    if new_top_2 > 2:
                        new_top_2 -= 1
                        count_left += 1
                        new_piece_2 -= 1
                    elif new_top_2 == 2 and new_piece_2 == 1 and news_broke_2 \
                            >= 2:
                        new_top_2 = 0
                        continue
                    else:
                        new_top_2 = 0
                        count_left += 2
                        new_piece_2 -= 2
                    news_broke_2 -= 1
            else:
                new_left_2 -= 1
                new_top_2 = top
                while new_top_2 and news_broke_2 and new_piece_2:
                    if new_top_2 > 2:
                        new_top_2 -= 1
                        count_left += 1
                        new_piece_2 -= 1
                    elif new_top_2 == 2 and new_piece_2 == 1 and news_broke_2 \
                            >= 2:
                        new_top_2 = 0
                        continue
                    else:
                        new_top_2 = 0
                        count_left += 2
                        new_piece_2 -= 2
                    news_broke_2 -= 1
# Сравниваем отломанные дольки по каждой грани с искомым количеством долек
if piece != count_top and piece != count_left \
        and piece != 1 or left == 0 or top == 0:
    print("Nelzya1")
elif piece == count_top and new_broke == 0\
        or piece == count_left and news_broke_2 == 0 or piece == 1:
    print("Mojno1")
elif piece == count_top and (left * new_top) % 2 == 0:
    # Далее идет проверка остатка дольковой площади на возможность разломать на
    # двойные дольки. Т.к. двойные - это не одинарные и являются наименьшими
    # возможными, то и проверка будет по ним. Не забывая, что (newn1 - 2) // 2
    # это остаток полосочки, если он не 2 то даст нам дополнительные надломы
    # -2 т.к. целочисленное деление от 2 даст 0, и от тройки также 0
    if (left * new_top / 2 - 1 + (new_left - 2) // 2) >= new_broke:  # -1 это
        # количество надломов меньше на 1 количества долек
        print("Mojno2")
    else:
        print("Nelzya2")
elif piece == count_left and (top * new_left_2) % 2 == 0:
    if (top * new_left_2 / 2 - 1 + (new_top_2 - 2) // 2) >= news_broke_2:
        # -1 это количество надломов меньше на 1 количества долек
        print("Mojno3")
    else:
        print("Nelzya3")
elif piece == count_top and (left * new_top - 1) % 2 == 0:  # нечетные
    if (left * new_top / 2 - 1 + (new_left - 2) // 2) >= new_broke:  # -1 это
        # количество надломов меньше на 1 количества долек
        print("Mojno4")
    else:
        print("Nelzya4")
elif piece == count_left and (top * new_left_2 - 1) % 2 == 0:  # нечетные
    if (top * new_left_2 / 2 - 1 + (new_top_2 - 2) // 2) >= news_broke_2:
        # -1 это количество надломов меньше на 1 количества долек
        print("Mojno5")
    else:
        print("Nelzya5")
else:
    print("Nelzya6")
