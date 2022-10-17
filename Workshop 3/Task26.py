# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Дарья, интуиция мне подсказывает, что задачу можно решить через формулу, но я по традиции собрал из костылей.

def fib_list(number) -> list:
    if number == 1:
        return [0, 1]
    elif number == 2:
        return [0, 1, 1]
    lst = fib_list(number - 1)
    lst.append(lst[-1] + lst[-2])
    return lst

def neg_fib_list(flst):
    nflst = []
    for i in range(1, len(flst)):
        if i % 2:
            nflst.append(flst[i])
        else:
            nflst.append(-flst[i])
    return nflst

def result_list(list1, list2):
    list2.reverse()
    result = list2 + list1
    return result

a = fib_list(int(input("Введите любое число: ")))
print(result_list(a, neg_fib_list(a)))