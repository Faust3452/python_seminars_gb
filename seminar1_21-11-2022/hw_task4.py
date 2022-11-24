# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

def which_quarter(check_num):
    if check_num == 1:
        print(f'для {check_num} четверти x > 0 и y > 0')
    if check_num == 2:
        print(f'для {check_num} четверти x < 0 и y > 0')
    if check_num == 3:
        print(f'для {check_num} четверти x < 0 и y < 0')
    if check_num == 4:
        print(f'для {check_num} четверти x > 0 и y < 0')


num_quarter = input('Введите номер четверти: ')
try:
    num_quarter = int(num_quarter)
    if num_quarter < 1 or num_quarter > 4:
        print('Вы ввели число, не обозначающее номер четверти!')
    else:
        which_quarter(num_quarter)
except Exception as e:
    print('Введены неверные данные!')