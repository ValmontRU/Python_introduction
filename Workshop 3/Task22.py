# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
my_list = [randint(0, 10) for i in range(10)]

def odd_index_sum(lst):
    sum = 0
    for item in range(len(lst)):
        if item % 2 != 0:
            sum += lst[item]
    print(sum)

print(my_list)
odd_index_sum(my_list)