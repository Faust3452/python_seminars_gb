# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4


check_x = input("Введите значение X: ")
check_y = input("Введите значение Y: ")
try:
    check_x = float(check_x)
    check_y = float(check_y)
    res = check_quarter(check_x, check_y)
    print(f'x = {check_x}; y = {check_y} -> {res}')
except Exception as e:
    print("Вы ввели неверные входные данные!")