# Codewars.com
# Create a method each_cons that accepts a list and a number n,
# and returns cascading subsets of the list of size n, like so:

# пока длина piece_list не сравняется с n, сохраняем в него все значения i,
# и когда заполнится до n, очищаем список.
# делаем клон списка my_list и в clone_list удаляем первое значение.
# в конечный список end_list сохраяняем все piece_list.
# цикл заканчивается когда в последнем списке списка end_list появляется 
# последняя
# цифра списка my_list, т.к. цикл идет до конца, пока не пройдет весь my_list


def each_cons(my_list, n):
    clone_list = my_list[0::]
    piece_list = []
    end_list = []
    for i in my_list:
        for j in clone_list:
            if len(piece_list) < n:
                piece_list.append(j)
            else:
                end_list.append(piece_list[0::])
                piece_list.clear()
                clone_list.remove(i)
                break
        if my_list[-1] in end_list[-1]:
            break
    return end_list


print(each_cons([int(i) for i in input().split()], int(input())))
