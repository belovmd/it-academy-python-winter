def euklid(first_num=None, second_num=None):
    if first_num is None:
        first_num = int(input('Введите число\n'))
    if second_num is None:
        second_num = int(input('Введите число\n'))
    while first_num and second_num:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    return first_num + second_num


def pair_elem(num_string=None):
    if num_string is None:
        num_string = input('Введите строку чисел через пробел\n')
    num_list = num_string.split()
    num_pair = 0
    check_list = num_list[:]
    for elem in num_list:
        check_list.remove(elem)
        num_pair += check_list.count(elem)
    return num_pair


def diff_words(input_string=None):
    if input_string is None:
        input_string = input('Введите строку\n')
    while input_string.find('  ') != -1 or input_string.find('\n') != -1:
        input_string = input_string.replace('\n', ' ')
        input_string = input_string.replace('  ', ' ')
    return len(set(input_string.split()))


def languages(*lang_list):
    if lang_list == ():
        langs = [{input('Введите язык\n') for _ in
                  range(int(input('Введите кол-во языков\n')))}
                 for _ in range(int(input('Введите кол-во школьников\n')))]
    else:
        langs = []
        language = set()
        for lang in lang_list:
            lang_list = lang.split(', ')
            language.update(lang_list)
            langs.append(language.copy())
            language.clear()

    lang_all = set.intersection(*langs)
    lang_one = set.union(*langs)
    return lang_all, lang_one
