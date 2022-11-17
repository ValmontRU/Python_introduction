from fractions import Fraction

def first_request():
    message = '''
    Выберите символ чисел, с которыми планируются арифметические действия:
    1 : Рациональные числа
    2 : Комплексные числа
    Ваш выбор: '''
    correct_choices = ['1', '2']
    choice = input(message)
    while choice not in correct_choices:
        print('Вы ввели неправильный символ. Повторите попытку.')
        choice = input(message)
    return choice

def ask_fraction_num1():
    m1 = int(input('Введите числитель 1-го числа: '))
    n1 = int(input('Введите знаменатель 1-го числа: '))
    while n1 == 0:
        print('Знаменатель не может быть равен нулю. Введите другое число.')
        n1 = int(input('Введите знаменатель 1-го числа: '))
    a = Fraction(m1, n1)
    return a

def ask_fraction_num2():
    m2 = int(input('Введите числитель 2-го числа: '))
    n2 = int(input('Введите знаменатель 2-го числа: '))
    while n2 == 0:
        print('Знаменатель не может быть равен нулю. Введите другое число.')
        n2 = int(input('Введите знаменатель 2-го числа: '))
    b = Fraction(m2, n2)
    return b

def compl1():
    a_compl = complex(input('Введите допустимый литерал 1-го комплексного числа: '))
    return a_compl

def compl2():
    b_compl = complex(input('Введите допустимый литерал 2-го комплексного числа: '))
    return b_compl

def ask_operation():
    message = '''
    Введите символ планируемой арифметической операции:
    + : Сложение
    - : Вычитание
    / : Деление
    * : Умножение
    Ваш выбор: '''
    correct_operations = ['+', '-', '/', '*']
    operation = input(message)
    while operation not in correct_operations:
        print('Вы ввели неправильный символ. Повторите попытку.')
        operation = input(message)
    return operation