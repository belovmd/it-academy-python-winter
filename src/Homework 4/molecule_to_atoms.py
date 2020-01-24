"""For a given chemical formula represented by a string, count the
number of atoms of each element contained in the molecule and return an
object (associative array in PHP, Dictionary<string, int> in C#,
Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside
the brackets tells you that you have to multiply count of each atom
inside the bracket on this index. For example, in Fe(NO3)2 you have one
iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested.
Index after the braces is optional.

https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python

"""

import re


def parse_molecule(formula):
    print(formula)
    # Меняем все скобки на круглые
    formula = re.sub(r'([[{])', r'(', formula)
    formula = re.sub(r'([]}])', r')', formula)
    # Проставляем * между не цифрами и цифрами
    formula = re.sub(r'(\D)(\d)', r'\1*\2', formula)
    # Заворачиваем элементы в кавычкм
    formula = re.sub(r'([A-Z]{1}[a-z]*)', r'"\1"', formula)
    # Расставляем плюсы между элементами, цифами и скобками
    formula = re.sub(r'([\")\d]{1})([\("]{1})', r'\1+\2', formula)
    formula = eval(formula)
    # Разбираем строку на элементы
    formula = re.findall(r'[A-Z]{1}[a-z]?', formula)
    dct = {}
    # Считаем кол-во элементов
    for el in formula:
        dct.setdefault(el, 0)
        dct[el] += 1
    return dct
