# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите любое число X: "))
y = int(input("Введите любое число Y: "))
z = int(input("Введите любое число Z: "))
check1 = not (x or y or z)
check2 = not x and not y and not z
if check1 == check2:
    print("Истинно")
else:
    print("Ложно")