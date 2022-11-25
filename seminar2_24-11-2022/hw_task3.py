# Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
#
# *Пример:*
#
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно


def generate_new_seq(n):
    return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]


num = 6
result = generate_new_seq(num)
sum = sum(result)
print(f'n = {num}: {result} -> {sum}')

