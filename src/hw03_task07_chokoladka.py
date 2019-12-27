"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите,
можно ли таким образом отломить от шоколадки ровно k долек.
Определите,
можно ли отломить от шоколадки ровно k одиночных долек
Определите,
можно ли отломить от шоколадки ровно k одиночных долек с помощью m разломов
Описание решение поместите в docstring
"""


shoko01 = int(input('размер шоколадки M:'))
shoko02 = int(input('размер шоколадки N:'))
doley = int(input('k - долек:'))
print(int(shoko01), int(shoko02), doley)
if doley <= shoko01 * shoko02 and shoko01 > 0 and shoko02 > 0:
    if (doley % shoko01 == 0 and doley >= shoko01) \
            or (doley % shoko02 == 0 and shoko01 <= doley):
        print('можно отломить', doley, 'долей за раз')
    else:
        print('за раз НЕ отломаешь', doley, 'долей')
if doley == shoko01 * shoko02:
    print('От шоколадки МОЖНО отломить ровно ', doley, 'одиночных долей')
else:
    print('НЕЛЬЗЯ отломить ровно', doley, 'одиночных  долей! '
                                          'Их ровно', shoko01 * shoko02)

razlomi = int(input('разломов:'))
if doley == razlomi and doley < shoko01 * shoko02:
    print('МОЖНО', doley, 'одиночных долей за', razlomi, 'разломов')
else:
    print('НЕЛЬЗЯ', doley, 'одиночных долей  за', razlomi, 'разломов')
max_razlomov = shoko01 * shoko02 - 1
