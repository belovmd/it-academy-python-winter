# 5. Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

print("Enter the input data, through 'Enter': ", sep='\n')
pupils = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone = set.intersection(*pupils)
known_by_someone = set.union(*pupils)
print(len(known_by_everyone), *known_by_everyone, sep='\n')
print(len(known_by_someone), *known_by_someone, sep='\n')
