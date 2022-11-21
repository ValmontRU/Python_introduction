import csv_module as cm

def pb_menu():
    while True:
        message = '''
        Выберите пункт меню, соответствующий желаемому действию:
            1. Показать все записи телефонной книги.
            2. Найти номер по фамилии.
            3. Найти номер по имени.
            4. Найти номер по отчеству.
            5. Поиск по номеру телефона.
            6. Добавить новую запись.
            7. Изменить существующую запись.
            8. Удалить запись.
            9. Закрыть программу.
        Ваш выбор: '''
        n = сheck_number(input(message))

        if n == 1:
            print(cm.retrive())
        elif n == 2:
            search = input('Введите фамилию: ')
            print(cm.retrive(surname=search))
        elif n == 3:
            search = input('Введите имя: ')
            print(cm.retrive(name=search))
        elif n == 4:
            search = input('Введите отчество: ')
            print(cm.retrive(second_name=search))
        elif n == 5:
            search = input('Введите номер  телефона: ')
            print(cm.retrive(number=search))
        elif n == 6:
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            second_name = input('Введите отчество: ')
            number = input('Введите номер телефона: ')
            cm.create(surname, name, second_name, number)
        elif n == 7:
            message2 = '''
            1. Найти номер по фамилии.
            2. Найти номер по имени.
            3. Найти по отчеству.
            4. Поиск по номеру телефона.
            Ваш выбор: '''
            change = сheck_number(input(message2))
            if change == 1:
                search = input('Введите фамилию: ')
                cm.retrive(surname=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cm.update(id=user_id, new_number=new_number)
            elif change == 2:
                search = input('Введите имя: ')
                cm.retrive(name=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cm.update(id=user_id, new_number=new_number)
            elif change == 3:
                search = input('Введите отчество: ')
                cm.retrive(second_name=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cm.update(id=user_id, new_number=new_number)
            elif change == 4:
                search = input('Введите номер телефона: ')
                cm.retrive(number=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cm.update(id=user_id, new_number=new_number)
            else:
                print('\nТакого пункта меню не существует.')
        elif n == 8:
            message3 = '''
            1. Найти номер по фамилии.
            2. Найти номер по имени.
            3. Найти по отчеству.
            4. Поиск по номеру телефона.
            Ваш выбор: '''
            delete = сheck_number(input(message3))
            if delete == 1:
                search = input('Введите фамилию: ')
                print(cm.retrive(surname=search))
                user_id = input('Введите id записи: ')
                cm.delete(id=user_id)
            elif delete == 2:
                search = input('Введите имя: ')
                print(cm.retrive(name=search))
                user_id = input('Введите id записи: ')
                cm.delete(id=user_id)
            elif delete == 3:
                search = input('Введите отчество: ')
                print(cm.retrive(second_name=search))
                user_id = input('Введите id записи: ')
                cm.delete(id=user_id)
            elif delete == 4:
                search = input('Введите номер телефона: ')
                print(cm.retrive(number=search))
                user_id = input('Введите id записи: ')
                cm.delete(id=user_id)
            else:
                print('\nТакого пункта меню не существует.')
        elif n == 9:
            break
        else:
            print('\nТакого пункта меню не существует.')

def сheck_number(num):
    while num.isdigit() != True:
        print('\nНеверный ввод.')
        num = input('Введите соответствующий пункт меню: ')
    return int(num)