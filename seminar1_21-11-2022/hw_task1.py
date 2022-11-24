# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def holiday_check_fn(num_day):
    if num_day > 0 and num_day < 8:
        if num_day == 6 or num_day == 7:
            print(f' {num_day} -> да')
        else:
            print(f' {num_day} -> нет')
    else:
        print('Вы ввели число, не обозначающее день недели')


day = input('Введите целое число, обозначающее день недели: ')
try:
    day = int(day)
    holiday_check_fn(day)
except Exception as e:
    print('Введено не целое значение, повторите ввод!')
