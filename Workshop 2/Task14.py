# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def digit_sum(number):
    sum = 0
    for digit in number:
        if digit.isdigit():
            sum += int(digit)
    print(sum)

digit_sum(input("Введите любое вещественное число: "))