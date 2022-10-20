# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def unique(lst):
    new_list = []
    for i in lst:
        if lst.count(i) == 1:
            new_list.append(i)
    print(new_list)

my_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7]
unique(my_list)