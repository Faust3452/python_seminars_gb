import random, math


def fill_mass_int(size, min, max):
    return [random.randint(min, max) for i in range(size)]


def fill_mass_float(size, min, max):
    return [round(random.randint(min, max) + random.random(), 2) for i in range(size)]


def odd_el_sum_count(check_list):
    sum = 0
    for i in range(len(check_list)):
        if i % 2 != 0:
            sum += check_list[i]
    return sum


def couple_multiple_count(check_list):
    result = list()
    for i in range(len(check_list) // 2):
        result.append(check_list[i] * check_list[-i-1])
    return result


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
        max = round(1 - (round(max) - max), 2)
    else:
        max = round(max - round(max), 2)
    if min - round(min) < 0:
        min = round(1 - (round(min) - min), 2)
    else:
        min = round(min - round(min), 2)
    print(f'fract max = {max}, fract min = {min}')
    return round(max - min, 2)


def binary_num(num):
    res = ''
    while num >= 1:
        res = res + str(num % 2)
        num = num // 2
    res = res[::-1]
    return res


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


if __name__ == "__main__":
    pass
