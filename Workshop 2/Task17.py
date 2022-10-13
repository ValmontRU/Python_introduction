# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на введенных пользователем позициях.

def random_multiplication(number):
    if number < 1:
        print("Вы ввели ненатуральное число")
    else:
        numberlist = list(range(-number, number + 1))
        i1 = int(input("Введите позицию 1-го элемента: "))
        i2 = int(input("Введите позицию 2-го элемента: "))
        if i1 > len(numberlist) or i1 < 1 or i2 > len(numberlist) or i2 < 1:
            print("Вы ввели позицию за пределами списка")
        else:
            print(numberlist)
            print(numberlist[i1 - 1] * numberlist[i2 - 1])

random_multiplication(int(input("Введите любое натуральное число: ")))