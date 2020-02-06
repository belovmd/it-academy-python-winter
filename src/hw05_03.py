"""
Реализовать функцию get_ranges
которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"

in_list - входящий список
upakovka - функция сворачивает список '-'
list_ordering - отправляем на упаковку
list_end - конечный список
"""


def get_ranges(in_list):
    def upakovka(ordering_list):
        if len(ordering_list) > 1:
            elementi_v_upakovke = str(ordering_list[0]) \
                                  + '-' + str(ordering_list[-1])
        else:
            elementi_v_upakovke = str(ordering_list[0])
        return elementi_v_upakovke
    list_ordering = []
    list_end = []
    for element in in_list:
        if len(list_ordering) == 0:
            list_ordering.append(element)
        elif list_ordering[-1] == element - 1:
            list_ordering.append(element)
        else:
            # отправляем на упаковку и очищаем список
            list_end.append(upakovka(list_ordering))
            list_ordering.clear()
            # запоминаем элемент на котором споткнулись
            list_ordering.append(element)
    list_end.append(upakovka(list_ordering))
    return ','.join(list_end)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
