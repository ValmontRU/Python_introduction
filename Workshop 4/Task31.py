# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def prime(number):
    if number < 1:
        print("Вы ввели ненатуральное число")
    else:
        lst = []
        x = 2
        while x ** 2 <= number:
            if number % x == 0:
                lst.append(x)
                number //= x
            else:
                x += 1
        if number >= 1:
            lst.append(number)
        print(lst)

prime(int(input("Введите любое натуральное число: ")))