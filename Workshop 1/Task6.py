# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input("Введите любое число от 1 до 7: "))
if number < 1 or number > 7:
    print("Вы ввели неправильное число")
elif number == 6 or number == 7:
    print("Да")
else:
    print("Нет")