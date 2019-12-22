"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите, можно ли таким образом отломить от шоколадки ровно k долек.
Определите, можно ли отломить от шоколадки ровно k одиночных долек
Определите, можно ли отломить от шоколадки ровно k одиночных долек
с помощью m разломов
"""

length = int(input('Введите длину шоколадки\n'))
width = int(input('Введите ширину шоколадки\n'))
pieces = int(input('Введите количество кусков\n'))

if pieces < length * width and (pieces % length == 0 or pieces % width == 0):
    print('Можно отломить {pieces} долек'.format(pieces=pieces))
else:
    print('Нельзя отломить {pieces} долек'.format(pieces=pieces))

if pieces <= length * width:
    print('Можно отломить {pieces} одиночных долек'.format(pieces=pieces))
else:
    print('Нельзя отломить {pieces} одиночных долек'.format(pieces=pieces))

cuts = int(input('Введите количество разломов\n'))
if pieces == length * width and cuts >= pieces - 1:
    print('Можно отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
elif pieces < length * width and (cuts <= (length * width) - 1) and \
        cuts >= pieces:
    print('Можно отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
else:
    print('Нельзя отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
