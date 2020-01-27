
import re


def dec(function):
    my_func_name = function.__name__
    dct_saves = {}

    def wrapper(*args, **kwargs):
        nonlocal dct_saves

        if my_func_name not in dct_saves:
            dct_saves.setdefault(my_func_name, [function(*args, **kwargs)])
        else:
            dct_saves[my_func_name].append(function(*args, **kwargs))
        return dct_saves

    return wrapper


@dec
def see_back(a=10, b=12):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


@dec
def words(text='qwere qwe asd'):
    text = set(re.findall(r'\b(\w+)\b', text))
    return len(text)


@dec
def order_list(my_list):
    for i in my_list:
        if i == 0:
            my_list.remove(i)
            my_list.append(i)
    return my_list


print(see_back(20, 15))
print(words('asd qwe zxc sd'))
print(see_back())
print(words())
print(order_list([1, 0, 2, 0, 3, 1, 2, 2, 3]))
print(order_list([1, 0, 2, 0, 3, 1, 0, 2, 2, 3, 1]))
print(see_back(20, 25))
