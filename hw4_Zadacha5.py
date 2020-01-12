pupils = int(input())
lang_list1 = []
all_lang = set()

for i in range(pupils):
    lang = int(input())
    lang_list = set()
    lang_list1.append(lang_list)
    for u in range(lang):
        q = input()
        lang_list.add(q)
        all_lang.add(q)

all_pup = lang_list1[0]

for j in range(len(lang_list1)):
    all_pup = lang_list1[j] & all_pup

print(len(all_pup))
for el in all_pup:
    print(el)

print(all_lang)
for el1 in all_lang:
    print(el1)
