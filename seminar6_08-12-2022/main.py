import math, functools


def couple_multiple_count(check_list):
    result = list()
    for i in range(len(check_list) // 2):
        result.append(check_list[i] * check_list[-i-1])
    return result


def couple_multiple_count_ver2(l: list):
    return [l[x] * l[-x-1] for x in range(len(l) // 2)]


def odd_el_sum_count(check_list):
    sum = 0
    for i in range(len(check_list)):
        if i % 2 != 0:
            sum += check_list[i]
    return sum


def odd_el_sum_count_ver2(l: list):
    return sum([l[i] for i in range(len(l)) if i % 2 != 0])


def diff_fraction_part(check_list):
    min = check_list[0]
    max = check_list[0]
    for i in range(1, len(check_list)):
        if check_list[i] > max:
            max = check_list[i]
        elif check_list[i] < min:
            min = check_list[i]
    print(f'max = {max}')
    print(f'min = {min}')
    if max - round(max) < 0:
        max = round(round(max) - max, 2)
    else:
        max = round(max - round(max), 2)
    if min - round(min) < 0:
        min = round(round(min) - min, 2)
    else:
        min = round(min - round(min), 2)
    return math.fabs(round(max - min, 2))


def diff_fraction_part_ver2(check_list):
    min = functools.reduce((lambda x, y: x if x < y else y), check_list)
    max = functools.reduce((lambda x, y: x if x > y else y), check_list)
    print(f'max = {max}')
    print(f'min = {min}')
    l = list(map(lambda x: round(math.fabs(round(x) - x), 2), [min, max]))
    return round(functools.reduce(lambda x, y: math.fabs(x - y), l), 2)


def fibonachi(num):
    fibo_negative = list()
    fibo_positive = list()
    for i in range(num):
        if i == 0:
            fibo_positive.append(1)
            fibo_negative.append(1)
        elif i == 1:
            fibo_positive.append(1)
            fibo_negative.append(-1)
        else:
            fibo_positive.append(fibo_positive[i-2] + fibo_positive[i-1])
            fibo_negative.append(int(math.pow(-1, i)*fibo_positive[-1]))
    fibo_negative = fibo_negative[::-1]
    fibo_negative.append(0)
    return fibo_negative+fibo_positive


def fibonachi_ver2(num):
    fibo_negative = list()
    fibo_positive = list()
    fibo_positive.extend([1, 1])
    [fibo_positive.append(fibo_positive[x-2] + fibo_positive[x-1]) for x in range(2, num)]
    [fibo_negative.insert(0, int(math.pow(-1, x) * fibo_positive[x])) for x in range(num)]
    fibo_negative.extend([0] + fibo_positive)
    return fibo_negative


def arith_count(s: str):
    s = s.split()
    i = 0
    l = len(s)
    while i < l - 1:
        if s[i] == '*':
            s[i-1] = float(s[i-1]) * float(s[i+1])
            s.pop(i)
            s.pop(i)
            i -= 1
        elif s[i] == '/':
            s[i - 1] = float(s[i - 1]) / float(s[i + 1])
            s.pop(i)
            s.pop(i)
            i -= 1
        else:
            i += 1
        l = len(s)
    l = len(s)
    while l != 1:
        if s[1] == '+':
            s[0] = float(s[0]) + float(s[2])
            s.pop(1)
            s.pop(1)
        elif s[1] == '-':
            s[0] = float(s[0]) - float(s[2])
            s.pop(1)
            s.pop(1)
        l = len(s)
    return round(s[0], 3)


def arith_count_with_brackets(s: str):
    brackets_pos = []
    for i in range(len(s) - 1):
        if s[i] == '(':
            j = i
            while s[j] != ')' and j != len(s) - 1:
                j += 1
            brackets_pos.append((i, j))
    d = dict()
    for i in brackets_pos:
        d[i] = s[i[0]:i[1]+1]
        d[i] = d[i].replace('(', '')
        d[i] = d[i].replace(')', '')
    tmp_l = []
    for i in d.keys():
        tmp_l.append(s[i[0]:i[1]+1])
    j = 0
    for i in d.keys():
        d[i] = arith_count(d[i])
        s = s.replace(tmp_l[j], str(d[i]))
        j += 1
    return arith_count(s)


if __name__ == "__main__":
    cmc = [2, 3, 4, 5, 6]
    print('Задача: найти произведение пар элементов списка')
    print(f'Версия исходная\n {cmc} -> {couple_multiple_count(cmc)}')
    print(f'Версия новая\n {cmc} -> {couple_multiple_count_ver2(cmc)}\n')
    print('Задача: найти сумму элементов списка, стоящих на нечетных позициях')
    oesc = [2, 3, 5, 9, 3]
    print(f'Версия исходная\n {oesc} -> {odd_el_sum_count(oesc)}')
    print(f'Версия новая\n {oesc} -> {odd_el_sum_count_ver2(oesc)}\n')
    print('Задача: найти разницу дробных частей максимального и минимального элементов списка')
    dfp = [1.1, 1.2, 3.1, 5, 10.01]
    print(f'Версия исходная\n {dfp} -> {diff_fraction_part(dfp)}')
    print(f'Версия новая\n {dfp} -> {diff_fraction_part_ver2(dfp)}\n')
    print('Задача: вычислить ряд Негафибоначчи для заданного k')
    k = 9
    print(f'Версия исходная\n для k = {k} -> {fibonachi(k)}')
    print(f'Версия новая\n для k = {k} -> {fibonachi_ver2(k)}\n')
    print('Задача: вычислить результат арифметического выражения, заданного строкой')
    ac = '1 + 2 * 3'
    acwb = '(1 + 2) * 3'
    print(f'Вариант без скобок, меняюших приоритет операций: {ac} = {arith_count(ac)}')
    print(f'Вариант со скобками, манящими приоритет операций: {acwb} = {arith_count_with_brackets(acwb)}\n')