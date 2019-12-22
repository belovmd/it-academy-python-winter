# Simple, remove the spaces from the string, then return the resultant string.
def no_space(x):
    s = x.replace(' ', '')
    # s = ""
    # for i in x:
    #     if i != " ":
    #         s += i
    return s


print(no_space('remove the spaces from the string'))
