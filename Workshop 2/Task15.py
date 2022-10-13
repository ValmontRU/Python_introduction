# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial_list(number):
    if number < 1:
        print("Вы ввели ненатуральное число")
    else:
        fact = 1
        factlist = []
        for i in range(1, number + 1):
            fact *= i
            factlist.append(fact)
        print(factlist)

factorial_list(int(input("Введите любое натуральное число: ")))