# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

import random


def making_new_rand_list(n):
    res = list()
    for i in range(n):
        res.append(random.randint(-n, n))
    return res


def multiple_from_file(check_list, filename ):
    mult = 1
    a = open(filename)
    for str in a:
        str = int(str)
        if str >= len(check_list):
            print(f' {str}: Данный индекс выходит за пределы диапазона индексов данного массива, \n поэтому индекс будет проигнорирован')
        else:
            mult = mult * check_list[str]
    return mult


def multiple_from_keyboard(check_list):
    mult = 1
    ind = input('Введите позиции индексов в строку через пробел (например: "0 1 3"): ')
    ind = ind.split(sep=" ")
    for i in ind:
        if i.isdigit() == True:
            i = int(i)
            if i > 0:
                if i >= len(check_list):
                    print(
                        f' {i}: Данный индекс выходит за пределы диапазона индексов данного массива, \n поэтому индекс будет проигнорирован')
                else:
                    mult = mult * check_list[i]
    return mult


input_number = input('Введите натуральное число: ')
input_number = int(input_number)
if input_number <= 0:
    print('Вы ввели отрицательное число, либо 0!')
else:
    new_list = making_new_rand_list(input_number)
    filepath = "D:\\Документы\\GB\\Python_learning\\seminar2_24-11-2022\\file.txt"
    mult_result = multiple_from_file(new_list, filepath)
    print(f'Сгенерированный список: {new_list}, произведение элементов = {mult_result}')
    mult_result = multiple_from_keyboard(new_list)
    print(f'Сгенерированный список: {new_list}, произведение элементов = {mult_result}')