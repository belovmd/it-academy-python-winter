# Read a given string, change the character at a given index
# and then print the modified string.
# replace the character at index i with character c.
def mutate_string(string, position, character):
    spis = list(s)
    spis[int(i)] = c
    spis="".join(spis)
    return(spis)
# блок ниже был уже в задаче
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
