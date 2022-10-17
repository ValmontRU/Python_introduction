# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def binary(decimal):
    result = ''
    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2
    print(result)

binary(int(input("Введите любое число: ")))