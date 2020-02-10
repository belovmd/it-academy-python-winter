# Даны два списка чисел. Посчитайте, сколько
# чисел входит только в один из этих списков

print(len(set(input("Please, enter some numbers").split()) 
& set(input("Please, enter some numbers").split())))
