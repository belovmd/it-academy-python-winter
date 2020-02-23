# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

pupils = int(input("Введите количество школьников: \n"))
lang_list1 = []
all_lang = set()

for i in range(pupils):
    lang = int(input("Введите кол-во языков школьника\n"))
    lang_list = set()
    lang_list1.append(lang_list)
    for _ in range(lang):
        language = input("Введите язык школьника:\n")
        lang_list.add(language)
        all_lang.add(language)

everybody_knows = lang_list1[0]

for j in range(len(lang_list1)):
    everybody_knows = lang_list1[j] & everybody_knows

print(len(everybody_knows))
for el in everybody_knows:
    print(el)

print(all_lang)
for el1 in all_lang:
    print(el1)
