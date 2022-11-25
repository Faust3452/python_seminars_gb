# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(number):
    res = 0
    new_num = str(number)
    for sim in new_num:
        if sim != "." and sim != "-":
            res += int(sim)
    return res


num = input('Введите вещественное число: ')
num = float(num)
result = sum_digits(num)
print(f'{num} -> {result}')
