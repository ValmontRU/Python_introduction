# *Реализуйте алгоритм перемешивания списка.

def list_shuffle(my_list):
    iteration = len(my_list)
    while iteration > 0:
        for i in range(1, len(my_list)):
            for j in range(1, len(my_list)):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
            iteration -= 1
    return my_list
    
list1 = [7, 3, 1, 8, 4, 2, 5, 9, 6, 0]
print(list1)
print(list_shuffle(list1))