# Simple, remove the spaces from the string, then return the resultant string.
def no_space(x):
    s = ""
    for i in x:
        if i != " ":
            s += i
    return s
