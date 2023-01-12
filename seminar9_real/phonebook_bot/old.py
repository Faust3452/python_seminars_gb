import methods
from telebot import TeleBot, types


def init_phonebook():
    return methods.make_numbers_list()


def UI(numbers):
    work = True
    print(numbers)
    while work:
        continue_ind = True
        inp_ind = True
        while inp_ind:
            try:
                inp = int(input("""
                        -------------------------------------------\n
                        Добро пожаловать в телефонный справочник!\n
                        Для выбора какого-либо пункта меню введите цифру, соотвутствующую пункту меню:\n
                        1. Просмотр телефонного справочника\n
                        2. Добавление записи\n
                        3. Импорт записей\n
                        4. Экспорт записей\n
                        5. Выход\n
                        -------------------------------------------\n
                        Дополнительно:\n
                        6. Поиск записей в справочнике\n
                        7. Удаление записи в справочнике\n
                        -------------------------------------------\n
                        Введите цифру: 
                        """))
                if inp in range(1, 8):
                    inp_ind = False
            except Exception as e:
                pass
        if inp == 5:
            print('До свидания!')
            work = False
            break
        if inp == 1:
            methods.show_numbers(numbers)
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 2:
            methods.add_record()
            numbers = methods.make_numbers_list()
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`, если хотите добавить еще одну запись - введите `ещё`: ")
                if d == 'назад':
                    continue_ind = False
                if d == 'ещё':
                    methods.add_record()
                    numbers = methods.make_numbers_list()
        if inp == 3:
            methods.import_record()
            numbers = methods.make_numbers_list()
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 4:
            methods.export_record('numbers.txt')
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 6:
            found = methods.search_records(numbers)
            if found != []:
                print('\nНиже представлена выборка из телефонного справочника, удовлетворяющая условиям поиска: ')
                methods.show_numbers(found)
            else:
                print('По вашему запросу не найдено записей в телефонном справочнике!')
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 7:
            methods.show_numbers(numbers)
            print('Для удаления из телефонного справочника (распечатан выше), необходимо сделать выборку, что будем удалять!')
            found = methods.search_records(numbers)
            if found != []:
                methods.delete_records(found, numbers)
                numbers = methods.make_numbers_list()
            else:
                print('По вашему запросу не найдено записей в телефонном справочнике!')

            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False