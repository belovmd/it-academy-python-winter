# In this little assignment you are given
# a string of space separated numbers,
# and have to return the highest and lowest
# number.
# high_and_low("1 2 3 4 5")
# return "5 1"

enter_string = input("Введите числа через пробел: ")
list_nums = [int(num) for num in enter_string.split()]
print(list_nums)
max_num = max(list_nums)
min_num = min(list_nums)
print(max_num, min_num)
