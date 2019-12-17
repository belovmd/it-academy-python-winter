string = "HELLO, My dear Friend!"
small = 0
big = 0
for char in string:
    if "A" <= char <= "Z":
        big += 1
    elif "a" < char < "z":
        small += 1
print("Количество строчных (маленьких) букв:", small)
print("Количество прописных (больших) букв", big)
