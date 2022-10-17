# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
my_list = [randint(0, 5) for i in range(5)]

def pair_multiplication(lst):
    result = []
    if len(lst) % 2 == 0:
        for item in range(int(len(lst) / 2)):
            result.append(lst[item] * lst[len(lst) - item - 1])
    else:
        for item in range(int(len(lst) / 2 + 1)):
            result.append(lst[item] * lst[len(lst) - item - 1])
    print(result)

print(my_list)
pair_multiplication(my_list)