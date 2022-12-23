from methods import *

def UI():
    people = people_init()
    work = True
    while work:
        continue_ind = True
        inp_ind = True
        while inp_ind:
            try:
                inp = int(input("""
                            -------------------------------------------\n
                            Меню просмотра информации о некоторой компании\n
                            Для выбора какого-либо пункта меню введите цифру, соотвутствующую пункту меню:\n
                            1. Просмотр списка сотрудников\n
                            2. Добавление сотрудника\n
                            3. Удаление сотрудника из списка\n
                            4. Просмотр состава отделов\n
                            5. Изменение данных сотрудника\n
                            6. Выход\n
                            -------------------------------------------\n
                            Введите цифру: 
                            """))
                if inp in range(1, 7):
                    inp_ind = False
            except Exception as e:
                pass
        if inp == 6:
            print('До свидания!')
            work = False
        if inp == 1:
            show_people(people)
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 2:
            people = add_person(people)
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 3:
            show_people(people)
            ind = True
            while ind:
                try:
                    index = int(input("Введите номер сотрудника для удаления из списка выше: "))
                    if index in range(1, len(people) + 1):
                        ind = False
                except Exception as e:
                    pass
            people = delete_person(people, index - 1)
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 4:
            show_departments(people)
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False
        if inp == 5:
            show_people(people)
            ind = True
            while ind:
                try:
                    index = int(input("Введите номер сотрудника для изменения его данных: "))
                    if index in range(1, len(people) + 1):
                        ind = False
                except Exception as e:
                    pass
            people = data_change(people, index - 1)
            while continue_ind:
                d = input("Для возвращения в главное меню наберите `назад`: ")
                if d == 'назад':
                    continue_ind = False


if __name__ == "__main__":
    UI()