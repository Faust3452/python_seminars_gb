# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def distance(x_a, y_a, x_b, y_b):
    return round(math.sqrt(pow(x_b - x_a, 2) + pow(y_b - y_a, 2)), 2)


x_first = input('Введите координату X первой точки: ')
y_first = input('Введите координату Y первой точки: ')
x_second = input('Введите координату X второй точки: ')
y_second = input('Введите координату Y второй точки: ')
try:
    x_first = float(x_first)
    y_first = float(y_first)
    x_second = float(x_second)
    y_second = float(y_second)
    dist = distance(x_first, y_first, x_second, y_second)
    print(f'A ({x_first};{y_first}); B ({x_second};{y_second}) -> {dist} ')
except Exception as e:
    print('Введены неверные входные данные!')