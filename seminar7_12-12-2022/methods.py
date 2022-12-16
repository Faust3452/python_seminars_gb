import os, shutil


def make_numbers_list(filename='numbers.txt'):
    with open(filename, encoding='utf-8') as f:
        s = f.read()
    s = s.split('%\n')
    s.remove('')
    for i in range(len(s)):
        s[i] = s[i].split('~')
    return s


def show_numbers(l: list):
    print('----Телефонный-справочник----\n')
    for i in range(len(l)):
        print(f'Запись №{i+1}:\n')
        print(f'Фамилия: {l[i][0]}\n')
        print(f'Имя: {l[i][1]}\n')
        print(f'Номер телефона: {l[i][2]}\n')
        print(f'Примечание: {l[i][3]}\n')
        if i != len(l) - 1:
            print('-----------------------------\n')
        else:
            print('------------Конец------------\n')



def add_record(phonebook='numbers.txt', surname='', name='', num='', info=''):
    tmp_l = []
    if surname == '' and name == '' and num == '' and info == '':
        print('Для добавления записи необходимо ввести фамилию, имя, телефонный номер и примечание для абонента')

        surname = input('Введите фамилию: ')
        check = True
        while check:
            acq = input('Подтвердите, что фамилия введена верно, если да, то введите `да`, чтобы исправить фамилию - введите `нет`: ' )
            if acq == 'да':
                check = False
            if acq == 'нет':
                surname = input('Введите фамилию: ')
        tmp_l.append(surname)

        name = input('Введите имя: ')
        check = True
        while check:
            acq = input('Подтвердите, что имя введено верно, если да, то введите `да`, чтобы исправить имя - введите `нет`: ' )
            if acq == 'да':
                check = False
            if acq == 'нет':
                name = input('Введите имя: ')
        tmp_l.append(name)

        num = input('Введите номер телефона: ')
        check = True
        while check:
            acq = input('Подтвердите, что номер телефона введен верно, если да, то введите `да`, чтобы исправить нмер телефона - введите `нет`: ')
            if acq == 'да':
                check = False
            if acq == 'нет':
                num = input('Введите номер телефона: ')
        tmp_l.append(num)

        info = input('Введите примечание: ')
        check = True
        while check:
            acq = input('Подтвердите, что примечание введено верно, если да, то введите `да`, чтобы исправить нмер телефона - введите `нет`: ')
            if acq == 'да':
                check = False
            if acq == 'нет':
                info = input('Введите примечание: ')
        tmp_l.append(info)
    else:
        tmp_l.extend([surname, name, num, info])

    with open(phonebook, mode='a+', encoding='utf-8') as f:
        f.write(f'{tmp_l[0]}~{tmp_l[1]}~{tmp_l[2]}~{tmp_l[3]}%\n')
    print('\nДанные успешно добавлены!\n')


def export_record(phonebook='numbers.txt'):
    inp_ind = True
    while inp_ind:
        try:
            fmt = int(input("""
            Для начала необходимо определить формат, в котором вы хотите получить справочник:\n
            1. Исходный формат, в котором хранится справочник (исходный)
            2. csv-формат
            3. json-формат
            4. xml-формат
            Введите цифру, соотвутствующую необходимому формату:
            """))
            if fmt in range(1, 5):
                inp_ind = False
        except Exception as e:
            pass
    filename = input('Введите имя для создаваемого на экспорт файла: ')
    if fmt == 1:
        open(filename + '.txt', mode='w', encoding='utf-8').close()
        shutil.copy(phonebook, filename + '.txt')
    if fmt == 2:
        with open(phonebook, encoding='utf-8') as f:
            with open(filename + '.csv', mode='w', encoding='utf-8') as new_f:
                wr_str = f.readlines()
                for l in wr_str:
                    l = l.replace('%\n', '')
                    l = l.split('~')
                    new_f.write(f'{l[0]};{l[1]};{l[2]};{l[3]}\n')
                new_f.close()
    if fmt == 3:
        op_file = '['
        cl_file = ']'
        op_obj = '{'
        cl_obj = '}'
        with open(phonebook, encoding='utf-8') as f:
            with open(filename + '.json', mode='w', encoding='utf-8') as new_f:
                new_f.write(op_file)
                wr_str = f.readlines()
                for l in range(len(wr_str)):
                    wr_str[l] = wr_str[l].replace('%\n', '')
                    wr_str[l] = wr_str[l].split('~')
                    if l != len(wr_str) - 1:
                        new_f.write(f"""\n\t{op_obj}"surname": "{wr_str[l][0]}", "name": "{wr_str[l][1]}", "number": "{wr_str[l][2]}", "info": "{wr_str[l][3]}"{cl_obj},""")
                    else:
                        new_f.write(f"""\n\t{op_obj}"surname": "{wr_str[l][0]}", "name": "{wr_str[l][1]}", "number": "{wr_str[l][2]}", "info": "{wr_str[l][3]}"{cl_obj}\n""")
                new_f.write(cl_file)
                new_f.close()
            f.close()
    if fmt == 4:
        op_tag = '<'
        cl_tag = '>'
        with open(phonebook, encoding='utf-8') as f:
            with open(filename + '.xml', mode='w', encoding='utf-8') as new_f:
                wr_str = f.readlines()
                new_f.write(f'{op_tag}phonebook{cl_tag}\n')
                for l in range(len(wr_str)):
                    wr_str[l] = wr_str[l].replace('%\n', '')
                    wr_str[l] = wr_str[l].split('~')
                    new_f.write(f'\t{op_tag}person{cl_tag}')
                    new_f.write(f"""\n\t\t{op_tag}surname{cl_tag}{wr_str[l][0]}{op_tag}/surname{cl_tag}\n\t\t{op_tag}name{cl_tag}{wr_str[l][1]}{op_tag}/name{cl_tag}\n\t\t{op_tag}number{cl_tag}{wr_str[l][2]}{op_tag}/number{cl_tag}\n\t\t{op_tag}info{cl_tag}{wr_str[l][3]}{op_tag}/info{cl_tag}\n""")
                    new_f.write(f'\t{op_tag}/person{cl_tag}\n')
                new_f.write(f'{op_tag}/phonebook{cl_tag}\n')
                new_f.close()
            f.close()


def import_record(phonebook='numbers.txt'):
    inp_ind = True
    while inp_ind:
        try:
            fmt = int(input("""
            Для начала необходимо определить формат, из которого вы хотите добавить данные в справочник:\n
            1. Исходный формат, в котором хранится справочник (исходный)
            2. csv-формат
            3. json-формат
            4. xml-формат
            Введите цифру, соотвутствующую необходимому формату:
            """))
            if fmt in range(1, 5):
                inp_ind = False
        except Exception as e:
            pass
    inp_ind = True
    filename = input("""Файл с имопртируемыми данными должен находиться в той же папке, что и исполняемый файл программы!'
                     Введите имя импортируемого фала без указания расширения (*.txt, *.csv, *.json): """)
    if fmt == 1:
        while inp_ind:
            if filename + '.txt' in os.listdir():
                inp_ind = False
            else:
                filename = input('Введите имя импортируемого фала без указания расширения (*.txt) или введите `стоп` для выхода в главное меню: ')
                if filename == 'стоп':
                    inp_ind = False
        if filename + '.txt' not in os.listdir():
            print('Возвращаемся в главное меню!')
        else:
            nl = make_numbers_list(filename=filename + '.txt')
            for i in nl:
                add_record(surname=i[0], name=i[1], num=i[2], info=i[3])
    if fmt == 2:
        while inp_ind:
            if filename + '.csv' in os.listdir():
                inp_ind = False
            else:
                filename = input('Введите имя импортируемого фала без указания расширения (*.csv) или введите `стоп` для выхода в главное меню: ')
                if filename == 'стоп':
                    inp_ind = False
        if filename + '.csv' not in os.listdir():
            print('Возвращаемся в главное меню!')
        else:
            with open(filename + '.csv', encoding='utf-8') as f:
                s = f.readlines()
                f.close()

            for l in range(len(s)):
                s[l] = s[l].replace('\n', '')
                s[l] = s[l].split(';')
                add_record(surname=s[l][0], name=s[l][1], num=s[l][2], info=s[l][3])
    if fmt == 3:
        while inp_ind:
            if filename + '.json' in os.listdir():
                inp_ind = False
            else:
                filename = input('Введите имя импортируемого фала без указания расширения (*.json) или введите `стоп` для выхода в главное меню: ')
                if filename == 'стоп':
                    inp_ind = False
        if filename + '.json' not in os.listdir():
            print('Возвращаемся в главное меню!')
        else:
            with open(filename + '.json', encoding='utf-8') as f:
                s = f.read()
                f.close()
            s = s.replace('\n', '')
            s = s.replace('\t', '')
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace('"', '')
            s = s.replace('{', '')
            s = s.replace('surname', '')
            s = s.replace('name', '')
            s = s.replace('number', '')
            s = s.replace('info', '')
            s = s.replace(' : ', '')
            s = s.replace(': ', '')
            s = s.split('},')
            s[-1] = s[-1].replace('}', '')
            for l in range(len(s)):
                s[l] = s[l].split(',')
                add_record(phonebook, surname=s[l][0], name=s[l][1], num=s[l][2], info=s[l][3])

    if fmt == 4:
        while inp_ind:
            if filename + '.xml' in os.listdir():
                inp_ind = False
            else:
                filename = input('Введите имя импортируемого фала без указания расширения (*.xml) или введите `стоп` для выхода в главное меню: ')
                if filename == 'стоп':
                    inp_ind = False
        if filename + '.xml' not in os.listdir():
            print('Возвращаемся в главное меню!')
        else:
            with open(filename + '.xml', encoding='utf-8') as f:
                s = f.read()
                f.close()
                s = s.replace('<phonebook>\n', '')
                s = s.replace('</phonebook>\n', '')
                s = s.replace('\n', '')
                s = s.replace('\t', '')
                s = s.replace('<person>', '<person>/')
                s = s.replace('</person>', '/')
                s = s.replace('<surname>', '/')
                s = s.replace('</surname>', '/')
                s = s.replace('<name>', '/')
                s = s.replace('</name>', '/')
                s = s.replace('<number>', '/')
                s = s.replace('</number>', '/')
                s = s.replace('<info>', '/')
                s = s.replace('</info>', '/')
                s = s.split('<person>')
                s.remove('')
                for l in range(len(s)):
                    s[l] = s[l].split('//')
                    s[l].remove('')
                    s[l].remove('')
                    add_record(surname=s[l][0], name=s[l][1], num=s[l][2], info=s[l][3])


def search_records(l: list):
    search_fields = [0 for i in range(4)]
    res_list = []
    inp_ind = True
    while inp_ind:
        try:
            inp = int(input("""Для поиска записей в справочнике, необходимо указать, по каким полям будет производиться поиск:
                      1. Фамилия
                      2. Имя
                      3. Номер телефона
                      4. Примечание
                      Введите цифру, соответствующую полю для поиска (далле можно будет добавить в поиск другие поля):
                      """))
            if inp in range(1, 5):
                search_fields[inp - 1] = 1
                one_more_ind = True
                while one_more_ind:
                    inp = input('Желаете ли вы добавить поле для поиска? Если да, то введите `да`, если нет, то введите что-нибудь отличное от `да`: ')
                    if inp == 'да':
                        try:
                            inp = int(input("""Для поиска записей в справочнике, необходимо указать, по каким полям будет производиться поиск:
                        1. Фамилия
                        2. Имя
                        3. Номер телефона
                        4. Примечание
                        Введите цифру, соответствующую полю для поиска (далле можно будет добавить в поиск другие поля):
                                      """))
                            if inp in range(1, 5):
                                search_fields[inp - 1] = 1
                        except Exception as e:
                            pass
                    else:
                        one_more_ind = False
                        inp_ind = False
        except Exception as e:
            pass
    for i in range(len(search_fields)):
        if search_fields[i] != 0:
            if i == 0:
                word = 'фамилия'
            if i == 1:
                word = 'имя'
            if i == 2:
                word = 'номер телефона'
            if i == 3:
                word = 'примечание'
            inp = input(f'Введите значение для поиска по полю "{word}": ')
            check = True
            while check:
                acq = input(f'Подтвердите, что значение для поиска по полю "{word}" верно, если да, то введите `да`, чтобы исправить значение - введите `нет`: ')
                if acq == 'да':
                    word = inp
                    check = False
                if acq == 'нет':
                    inp = input(f'значение для поиска по полю "{word}": ')
            search_fields[i] = word
    first_non_zero_index = -1
    first_ind = True
    i = 0
    while first_ind:
        if search_fields[i] != 0:
            first_non_zero_index = i
            first_ind = False
        i += 1
    if first_non_zero_index == -1:
        return res_list
    else:
        for i in range(len(l)):
            if l[i][first_non_zero_index] == search_fields[first_non_zero_index]:
                if l[i] not in res_list:
                    res_list.append(l[i])
        for i in range(first_non_zero_index + 1, len(search_fields)):
            if search_fields[i] != 0:
                for s in res_list:
                    if search_fields[i] != s[i]:
                        res_list.remove(s)
    return res_list


def delete_records(l_delete: list, l_where_delete: list, filename='numbers.txt'):
    for i in l_delete:
        l_where_delete.remove(i)
    f = open(filename, mode='w', encoding='utf-8').close()
    with open(filename, mode='w', encoding='utf-8') as f:
        for i in l_where_delete:
            add_record(surname=i[0], name=i[1], num=i[2], info=i[3])
    print('Данные удалены из справочника!')