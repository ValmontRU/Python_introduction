# Создайте программу для игры с конфетами человек против бота.
# Отличие от игры против человека (кроме имени) в строке 35 - происходит рандомный выбор числа конфет.

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмёте - от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. На столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Бот"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Победитель - {player1}")
else:
    print(f"Победитель - {player2}")