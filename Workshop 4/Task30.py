# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

# Дарья, созданный файл в стандартном блокноте открывается вполне читабельным.
# В VS Code (у меня) открываются крокозябры, но с кодировкой разбираться не стал, т.к. см. выше.

def list_from_txt(path):
    data = open(path, 'r', encoding='utf-8')
    lst = [line.strip() for line in data]
    data.close()
    return lst

def create_dict(lst1, lst2):
    new_dict = dict(zip(lst1, lst2))
    with open('users_hobby.txt', 'x') as new_file:
        for key, value in new_dict.items():
            new_file.write(f'{key}: {value}\n')

users = list_from_txt('users.txt')
hobby = list_from_txt('hobby.txt')

create_dict(users, hobby)