"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите, можно ли таким образом отломить от шоколадки ровно k долек.
Определите, можно ли отломить от шоколадки ровно k одиночных долек
Определите, можно ли отломить от шоколадки ровно k одиночных долек
с помощью m разломов
"""
import sys

length = int(input('Введите длину шоколадки\n'))
width = int(input('Введите ширину шоколадки\n'))
pieces = int(input('Введите количество кусков\n'))
choc_sum = length * width
#  проверяем чтобы кол-во долек не превышало общее их число
if pieces > choc_sum:
    print('Слишком много хотите')
    sys.exit(0)

#  кратность кол-ва долек длине или ширине
#  Определите, можно ли таким образом отломить от шоколадки ровно k долек
if pieces != choc_sum and (pieces % length == 0 or pieces % width == 0):
    print('Можно отломить {pieces} долек одним разломом'.
          format(pieces=pieces))
else:
    print('Нельзя отломить {pieces} долек одним разломом'.
          format(pieces=pieces))

#  Определите, можно ли отломить от шоколадки ровно k одиночных долек
if pieces <= choc_sum:
    print('Можно отломить {pieces} одиночных долек'.format(pieces=pieces))

cuts = int(input('Введите количество разломов\n'))

"""
если мы хотим все кусочки, то мин число разломов равно на 1 меньше всех кусков
если кол-во кусков кратно сторонам шоколадки, то мин число разломов такое же
если кол-во кусков подходит к краям шоколада, то кол-во разломов такое же
в остальных случаях кол-во разломов на 1 больше кол-ва кусков
"""

#  Можно ли отломить от шоколадки ровно k одиночных долек за m разломов
if pieces == choc_sum and cuts >= pieces - 1:
    print('Можно отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
elif pieces % length == 0 or pieces % width == 0 and cuts >= pieces:
    print('Можно отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
elif cuts >= pieces and \
        (pieces > choc_sum - length or pieces > choc_sum - width):
    print('Можно отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
elif cuts >= pieces + 1:
    print('Можно отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
else:
    print('Нельзя отломить {pieces} долек за {cuts} разломов'.
          format(pieces=pieces, cuts=cuts))
