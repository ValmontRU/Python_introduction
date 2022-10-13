# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Дарья, добиться строгого соответствия ТЗ касательно визуального представления итогового результата
# я смог только с нагромождением костылей из временных переменных, обрабатывающих строки. Не обессудьте.

def function_list(number):
    if number < 1:
        print("Вы ввели ненатуральное число")
    else:
        flist = []
        for i in range(1, number + 1):
            result = (1 + 1 / i) ** i
            temp1 = [i, round(result, 2)]
            temp2 = str(temp1)
            temp3 = temp2.replace(',', ':')
            flist.append(temp3)
        temp4 = str(flist)
        temp5 = temp4.replace("'[", "")
        temp6 = temp5.replace("]'", "")
        print(temp6)

function_list(int(input("Введите любое натуральное число: ")))