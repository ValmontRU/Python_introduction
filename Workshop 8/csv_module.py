import csv
import os.path

db_file_name = ''
db = []
global_id = 0

def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', encoding='utf-8', newline='').close()


def create(surname='', name='', second_name='', number=''):
    global global_id
    global db
    global db_file_name
    if(surname == ''):
        print("Фамилия не введена")
        return
    if(name == ''):
        print("Имя не введено")
        return
    if(second_name == ''):
        print("Отчество не введено")
        return
    if(number == ''):
        print("Номер телефона не введён")
        return
    for row in db:
        if(row[1] == surname.title() and row[2] == name.title() and row[3] == second_name.title() and row[4] == number):
            print("Уже в справочнике")
            return
    global_id += 1
    new_row = [str(global_id), surname.title(), name.title(),
               second_name.title(), number]
    db.append(new_row)
    with open(db_file_name, 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)

def retrive(id='', surname='', name='', second_name='', number=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(surname != '' and row[1] != surname.title()):
            continue
        if(name != '' and row[2] != name.title()):
            continue
        if(second_name != '' and row[3] != second_name.title()):
            continue
        if(number != '' and row[4] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result

def update(id='', new_surname='', new_name='', new_second_name='', new_number=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('Уточните id')
        return
    with open(db_file_name, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_surname != ''):
                    row[1] = new_surname.title()
                if(new_name != ''):
                    row[2] = new_name.title()
                if(new_second_name != ''):
                    row[3] = new_second_name.title()
                if(new_number != ''):
                    row[4] = new_number
            writer.writerow(row)

def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('Уточните id')
        return
    for row in db:
        if (row[0] == id):
            db.remove(row)
            break
    with open(db_file_name, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)