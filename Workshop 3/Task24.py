# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform
my_list = [round(uniform(0, 5), 2) for i in range(5)]

def dif_max_min(lst):
    temp = [round(j%1, 2) for j in lst if j%1 != 0]
    print(max(temp) - min(temp))

print(my_list)
dif_max_min(my_list)