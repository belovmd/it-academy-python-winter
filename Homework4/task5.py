# 5. Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

pupils = [{input('Enter the language: ')
           for language in range(int(input('Number of languages Mi: ')))}
          for pupil in range(int(input('Number of pupils N: ')))]
known_by_everyone = set.intersection(*pupils)
known_by_someone = set.union(*pupils)
print(len(known_by_everyone), *known_by_everyone, sep='\n')
print(len(known_by_someone), *known_by_someone, sep='\n')
