# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер координатной четверти: "))
if quarter < 1 or quarter > 4:
    print("Вы ввели неправильное значение координатной четверти")
elif quarter == 1:
    print("X и Y положительные")
elif quarter == 2:
    print("X отрицательное, Y положительное")
elif quarter == 3:
    print("X и Y отрицательные")
else:
    print("X положительное, Y отрицательное")