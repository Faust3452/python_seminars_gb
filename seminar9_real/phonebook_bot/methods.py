import os
import shutil


def make_numbers_list(filename='numbers.txt'):
    with open(filename, encoding='utf-8') as f:
        s = f.read()
    s = s.split('%\n')
    s.remove('')
    for i in range(len(s)):
        s[i] = s[i].split('~')
    return s


def show_numbers(l: list, num=''):
    if num != '':
        return f'Запись №{num}\nФамилия: {l[0]}\nИмя: {l[1]}\nНомер телефона: {l[2]}\nПримечание: {l[3]}\n'
    else:
        return f'Фамилия: {l[0]}\nИмя: {l[1]}\nНомер телефона: {l[2]}\nПримечание: {l[3]}\n'



def add_record(phonebook='numbers.txt', surname='', name='', num='', info=''):
    tmp_l = []
    tmp_l.extend([surname, name, num, info])
    with open(phonebook, mode='a+', encoding='utf-8') as f:
        f.write(f'{tmp_l[0]}~{tmp_l[1]}~{tmp_l[2]}~{tmp_l[3]}%\n')
    print('\nДанные успешно добавлены!\n')


def export_record(fmt, phonebook='numbers.txt', filename='data'):
    if fmt == 1:
        open(filename + '.txt', mode='w', encoding='utf-8').close()
        shutil.copy(phonebook, filename + '.txt')
        return filename + '.txt'
    if fmt == 2:
        with open(phonebook, encoding='utf-8') as f:
            with open(filename + '.csv', mode='w', encoding='utf-8') as new_f:
                wr_str = f.readlines()
                for l in wr_str:
                    l = l.replace('%\n', '')
                    l = l.split('~')
                    new_f.write(f'{l[0]};{l[1]};{l[2]};{l[3]}\n')
                new_f.close()
        return filename + '.csv'
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
        return filename + '.json'
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
        return filename + '.xml'


def import_record(fmt, filename, phonebook='numbers.txt'):
    if fmt == 1:
            nl = make_numbers_list(filename=filename)
            for i in nl:
                add_record(surname=i[0], name=i[1], num=i[2], info=i[3])
    if fmt == 2:
        with open(filename, encoding='utf-8') as f:
            s = f.readlines()
            f.close()

        for l in range(len(s)):
            s[l] = s[l].replace('\n', '')
            s[l] = s[l].split(';')
            add_record(surname=s[l][0], name=s[l][1], num=s[l][2], info=s[l][3])
    if fmt == 3:
        with open(filename, encoding='utf-8') as f:
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
        with open(filename, encoding='utf-8') as f:
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

def search(l: list, search_obj: list):
    res = []
    for i in range(len(l)):
        tmp = [str(l[i][j]) for j in range(len(l[i]))]
        for k in range(len(search_obj)):
            if search_obj[k] in tmp:
                res.append(tmp)
    return res


def search_records(l: list, search_fields: list):
    res_list = []
    # inp_ind = True
    # while inp_ind:
    #     try:
    #         inp = int(input("""Для поиска записей в справочнике, необходимо указать, по каким полям будет производиться поиск:
    #                   1. Фамилия
    #                   2. Имя
    #                   3. Номер телефона
    #                   4. Примечание
    #                   Введите цифру, соответствующую полю для поиска (далле можно будет добавить в поиск другие поля):
    #                   """))
    #         if inp in range(1, 5):
    #             search_fields[inp - 1] = 1
    #             one_more_ind = True
    #             while one_more_ind:
    #                 inp = input('Желаете ли вы добавить поле для поиска? Если да, то введите `да`, если нет, то введите что-нибудь отличное от `да`: ')
    #                 if inp == 'да':
    #                     try:
    #                         inp = int(input("""Для поиска записей в справочнике, необходимо указать, по каким полям будет производиться поиск:
    #                     1. Фамилия
    #                     2. Имя
    #                     3. Номер телефона
    #                     4. Примечание
    #                     Введите цифру, соответствующую полю для поиска (далле можно будет добавить в поиск другие поля):
    #                                   """))
    #                         if inp in range(1, 5):
    #                             search_fields[inp - 1] = 1
    #                     except Exception as e:
    #                         pass
    #                 else:
    #                     one_more_ind = False
    #                     inp_ind = False
    #     except Exception as e:
    #         pass
    # for i in range(len(search_fields)):
    #     if search_fields[i] != 0:
    #         if i == 0:
    #             word = 'фамилия'
    #         if i == 1:
    #             word = 'имя'
    #         if i == 2:
    #             word = 'номер телефона'
    #         if i == 3:
    #             word = 'примечание'
    #         inp = input(f'Введите значение для поиска по полю "{word}": ')
    #         check = True
    #         while check:
    #             acq = input(f'Подтвердите, что значение для поиска по полю "{word}" верно, если да, то введите `да`, чтобы исправить значение - введите `нет`: ')
    #             if acq == 'да':
    #                 word = inp
    #                 check = False
    #             if acq == 'нет':
    #                 inp = input(f'значение для поиска по полю "{word}": ')
    #         search_fields[i] = word
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