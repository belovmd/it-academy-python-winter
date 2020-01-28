def get_ranges(lst_1=[int(el) for el in input().split()]):
    lst_1 = sorted(lst_1)
    new_str = ""
    for el in lst_1:
        try:
            if el == lst_1[0]:
                new_str = new_str + str(el)
            elif el + 1 == int(lst_1[lst_1.index(el) + 1])\
                    and (int(el) - 1) == int(lst_1[lst_1.index(el) - 1]):
                new_str + ""
            elif (int(el) + 1) != int(lst_1[lst_1.index(el) + 1]) \
                    and (int(el) - 1) == int(lst_1[lst_1.index(el) - 1]):
                new_str = new_str + "-" + str(el)
            elif (int(el) + 1) != int(lst_1[lst_1.index(el) + 1]) \
                    and (int(el) - 1) != int(lst_1[lst_1.index(el) - 1]):
                new_str = new_str + "," + str(el)
            else:
                new_str = new_str + "," + str(el)
        except IndexError:
            if el - 1 == int(lst_1[lst_1.index(el) - 1]):
                new_str = new_str + "-" + str(el)
            else:
                new_str = new_str + "," + str(el)
    return new_str


print(get_ranges())
