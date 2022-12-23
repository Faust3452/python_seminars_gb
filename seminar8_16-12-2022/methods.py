from classes import *


def show_people(people: list):
    for i in range(len(people)):
        print(f'Сотрудник № {i+1}')
        people[i].show_info()


def people_init():
    with open('people.csv', encoding='utf-8') as f:
        f = f.readlines()
        for i in range(len(f)):
            f[i] = f[i].replace('\n', '')
            f[i] = f[i].split(';')
            f[i] = Person(name=f[i][0], age=int(f[i][1]), gender=f[i][2], department=f[i][3], status=f[i][4])
    return f


def delete_person(people: list, index):
    people.remove(people[index])
    with open('people.csv', mode='w', encoding='utf-8') as f:
        for i in people:
            f.write(f'{i.name};{i.age};{i.gender};{i.department};{i.status}\n')
    return people


def add_person(people: list):
    new_person = []
    print('Для того, чтобы добавить  человека в список компании, нужно ввести следующие данные: имя, возраст, пол, отдел, должность!\nПоехали!')
    new_person.append(input('Введите имя нового сотрудника: '))
    ind = True
    while ind:
        try:
            inp = int(input('Введите возраст нового сотрудника: '))
            ind = False
            new_person.append(inp)
        except Exception as e:
            pass
    ind = True
    while ind:
        try:
            inp = input('Введите пол нового сотрудника (`муж` или `жен`): ')
            if inp == 'муж' or inp == 'жен':
                ind = False
                new_person.append(inp)
        except Exception as e:
            pass
    new_person.append(input('Введите наименование отдела, в котором работает новый сотрудник: '))
    new_person.append(input('Введите должность, в которой состоит новый сотрудник: '))
    print(new_person)
    ind = True
    for i in range(len(people)):
        if Person(new_person[0], new_person[1], new_person[2], new_person[3], new_person[4]) == people[i]:
            ind = False
            print('Этот сотрудник уже находится в списке!')
    if ind:
        people.append(Person(new_person[0], new_person[1], new_person[2], new_person[3], new_person[4]))
        with open('people.csv', mode='w', encoding='utf-8') as f:
            for i in people:
                f.write(f'{i.name};{i.age};{i.gender};{i.department};{i.status}\n')
    return people


def show_departments(people: list):
    dep_list = []
    for i in range(len(people)):
        if people[i].department not in dep_list:
            dep_list.append(people[i].department)
    print('Список отделов: ')
    for i in range(len(dep_list)):
        print(f'Отдел № {i+1}: {dep_list[i]}')
    ind = True
    while ind:
        try:
            inp = int(input('Введите номер отдела из списка выше, чтобы посомтреть его состав: '))
            if inp in range(1, len(dep_list) + 1):
                ind = False
                inp -= 1
        except Exception as e:
            pass
    count_members = 1
    for i in range(len(people)):
        if people[i].department == dep_list[inp]:
            print(f'Сотрудник № {count_members}')
            people[i].show_info()
            count_members += 1


def data_change(people: list, index):
    change_data = []
    print("""
    Выберите данные, которые вы хотите изменить:
    1. Возраст
    2. Отдел, в котором работает сотрудник
    3. Должность, в которой состоит сотрудник
    Для этого введите цифру, соответствующую данным, которые вы хотите изменить.
    """)
    ind = True
    while ind:
        try:
            inp = int(input('Введите цифру: '))
            if inp in range(1, 4):
                if inp not in change_data:
                    change_data.append(inp)
                inp = input('Хотите ли вы добавить еще данные? Eсли да, то введите `да`, если нет, то введите что-угодно: ')
                if inp != 'да':
                    ind = False
        except Exception as e:
            pass
    for i in range(len(change_data)):
        if change_data[i] == 1:
            ind = True
            while ind:
                try:
                    inp = int(input('Введите новый возраст: '))
                    ind = False
                    change_data[i] = (change_data[i], inp)
                except Exception as e:
                    pass
        if change_data[i] == 2:
            inp = input('Введите название нового отдела для сотрудника: ')
            change_data[i] = (change_data[i], inp)
        if change_data[i] == 3:
            inp = input('Введите название новой должности для сотрудника: ')
            change_data[i] = (change_data[i], inp)
    for i in range(len(change_data)):
        if change_data[i][0] == 1:
            people[index].age = change_data[i][1]
        if change_data[i][0] == 2:
            people[index].department = change_data[i][1]
        if change_data[i][0] == 3:
            people[index].status = change_data[i][1]
    with open('people.csv', mode='w', encoding='utf-8') as f:
        for i in people:
            f.write(f'{i.name};{i.age};{i.gender};{i.department};{i.status}\n')
    return people


if __name__ == "__main__":
    pass