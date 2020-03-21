# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
people = int(input("Кол-во школьников: "))
lang_list1 = []
full_lang = set()

for i in range(people):
    all_lang = int(input("Введите кол-во языков школьника: "))
    lang_list2 = set()
    lang_list1.append(lang_list2)
    for _ in range(all_lang):
        language = input("Введите язык школьника: ")
        lang_list2.add(language)
        full_lang.add(language)

everybody_knows = lang_list1[0]

for j in range(len(lang_list1)):
    everybody_knows = lang_list1[j] & everybody_knows

print('Кол-во языков которые знаю все школьники:', len(everybody_knows))
print('Список этих языков:', end=' ')
for answer1 in everybody_knows:
    print(answer1)

print('Кол-во языков которые знает хоть один школьник:', len(full_lang))
print('Список этих языков:', end=' ')
for answer2 in full_lang:
    print(answer2)
