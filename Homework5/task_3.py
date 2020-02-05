# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел, отсортированных по
# возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(inp_lst):
    outp_lst = []
    for i in range(0, len(inp_lst)):
        if i != 0 and i != len(inp_lst) - 1:
            if inp_lst[i] - inp_lst[i - 1] == 1 and \
                    inp_lst[i + 1] - inp_lst[i] == 1:
                outp_lst.append('-')
            elif inp_lst[i] - inp_lst[i - 1] != 1 and \
                    inp_lst[i + 1] - inp_lst[i] == 1:
                outp_lst.append(str(inp_lst[i]))
                outp_lst.append('-')
            elif inp_lst[i] - inp_lst[i - 1] == 1 and \
                    inp_lst[i + 1] - inp_lst[i] != 1:
                outp_lst.append('-')
                outp_lst.append(str(inp_lst[i]))
            else:
                outp_lst.append(str(inp_lst[i]))
        else:
            outp_lst.append(str(inp_lst[i]))
    # print(outp_lst)

    # remove needless '-'
    finish_lst = []

    for i in range(0, len(outp_lst)):
        if outp_lst[i] != outp_lst[i - 1]:
            if outp_lst[i - 1] == '-' and i != len(outp_lst) - 1:
                finish_lst.append(outp_lst[i])
                finish_lst.append(',')
            else:
                finish_lst.append(outp_lst[i])
                finish_lst.append(',')

    output_string = ''.join(finish_lst)
    output_string = output_string.replace(',-,', '-')
    output_string = output_string.rstrip(',')
    return output_string


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
