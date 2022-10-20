# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
import itertools

def new_polynomial(k, ratios):
    if k < 1:
        print("Вы ввели ненатуральное число")
    else:
        f = ['*x^']*(k-1) + ['*x']
        polynom = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, f, range(k, 1, -1), fillvalue='') if a != 0]
        for x in polynom:
            x.append(' + ')
        polynom = list(itertools.chain(*polynom))
        polynom[-1] = ' = 0'
        return "".join(map(str, polynom)).replace(' 1*x', ' x')

k = int(input("Введите любое натуральное число: "))
ratios = [randint(0, 100) for i in range(k + 1)]
polynomial = new_polynomial(k, ratios)

with open('task33.txt', 'x') as data:
    data.write(polynomial)