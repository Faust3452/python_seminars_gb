import math, random, os


def polynome_to_file_write(pow, filename = "new.txt"):
    pow_list = [random.randint(0, 100) for i in range(pow + 1)]
    if pow_list[pow] == 0:
        while pow_list[pow] == 0:
            pow_list[pow] = random.randint(0, 100)
    print(f'Список коэффициентов: {pow_list}')
    degree = pow
    poly = ''
    for i in range(len(pow_list)):
        if i == len(pow_list) - 1 and pow_list[i] != 0:
            poly += str(pow_list[i])
        elif i == 0:
            poly += str(pow_list[i]) + f'*x^{degree}' + ' + '
        else:
            poly += str(pow_list[i]) + f'*x^{degree}' + ' + '
        degree -= 1
    poly += ' = 0'
    print(poly)
    with open(filename, mode='w') as f:
        f.write(poly)


def fill_mass_int(size, min, max):
    return [random.randint(min, max) for i in range(size)]


def fill_mass_float(size, min, max):
    return [round(random.randint(min, max) + random.random(), 2) for i in range(size)]


def non_repeating_el(check_list):
    result = list()
    [result.append(check_list[i]) for i in range(len(check_list)) if check_list[i] not in result]
    return result


def simple_factor(num):
    factor = list()
    delim = 2
    while num != 1:
        if num % delim == 0:
            num = num // delim
            factor.append(delim)
            delim = 2
        else:
            delim += 1
    return factor


def pi_with_precision(eps):
    pi = 0
    delim = 1
    sgn = 1
    a = 4 / delim
    while a > eps:
        a = 4 / delim
        pi = pi + sgn * a
        sgn = -sgn
        delim = delim + 2
    return pi


def sum_poly(filename1, filename2, filename3="sum_poly.txt"):
    f1 = open(filename1).read()
    print(f1)
    f2 = open(filename2).read()
    print(f2)
    f1 = f1.replace('= 0', '')
    f2 = f2.replace('= 0', '')
    f1 = f1.replace('*x^', '^')
    f1 = f1.replace('*x', 'x')
    f1 = f1.replace(' ', '')
    f1 = f1.replace('-', '+-')
    f1 = f1.split('+')
    f2 = f2.replace('*x^', '^')
    f2 = f2.replace('*x', 'x')
    f2 = f2.replace(' ', '')
    f2 = f2.replace('-', '+-')
    f2 = f2.split('+')

    for i in range(len(f1)):
        f1[i] = f1[i].split('^')
    for i in range(len(f2)):
        f2[i] = f2[i].split('^')

    f1_degree = [0 for i in range(int(f1[0][1]) + 1)]
    f2_degree = [0 for i in range(int(f2[0][1]) + 1)]

    for i in range(len(f1)):
        if len(f1[i]) == 2:
            f1_degree[int(f1[i][1])] = f1[i][0]
        else:
            if 'x' in f1[i][0]:
                f1[i] = f1[i][0].replace('x', '')
                if f1[i] == '':
                    f1[i] = '1'
                f1_degree[1] = f1[i]
            else:
                f1_degree[0] = f1[i][0]

    for i in range(len(f2)):
        if len(f2[i]) == 2:
            f2_degree[int(f2[i][1])] = f2[i][0]
        else:
            if 'x' in f2[i][0]:
                f2[i] = f2[i][0].replace('x', '')
                if f2[i] == '':
                    f2[i] = '1'
                f2_degree[1] = f2[i]
            else:
                f2_degree[0] = f2[i][0]

    for i in range(len(f1_degree)):
        if str(type(f1_degree[i])) == "<class 'str'>":
            if f1_degree[i].isdigit():
                f1_degree[i] = int(f1_degree[i])
            else:
                f1_degree[i] = -int(f1_degree[i].replace('-', ''))

    for i in range(len(f2_degree)):
        if str(type(f2_degree[i])) == "<class 'str'>":
            if f2_degree[i].isdigit():
                f2_degree[i] = int(f2_degree[i])
            else:
                f2_degree[i] = -int(f2_degree[i].replace('-', ''))

    if len(f1_degree) > len(f2_degree):
        for i in range(len(f2_degree)):
            f1_degree[i] = f1_degree[i] + f2_degree[i]
            newl = f1_degree
    else:
        for i in range(len(f1_degree)):
            f2_degree[i] = f2_degree[i] + f1_degree[i]
            newl = f2_degree

    poly = ''
    i = len(newl) - 1
    while i >= 0:
        if i == 0 and newl[i] != 0:
            if newl[i] < 0:
                poly += f'{str(newl[i])}'
            else:
                poly += f'+{str(newl[i])}'
        else:
            if i == 1 and newl[i] != 0:
                if newl[i] < 0:
                    poly += f'{str(newl[i])}*x'
                else:
                    poly += f'+{str(newl[i])}*x'
            else:
                if i == len(newl) - 1 and newl[i] != 0:
                    if newl[i] < 0:
                        poly += f'{str(newl[i])}*x^{i}'
                    else:
                        poly += f'{str(newl[i])}*x^{i}'
                else:
                    if newl[i] != 0:
                        if newl[i] < 0:
                            poly += f'{str(newl[i])}*x^{i}'
                        else:
                            poly += f'+{str(newl[i])}*x^{i}'

        i -= 1
    poly += ' = 0'
    print(poly)
    with open(filename3, mode='w') as f:
        f.write(poly)



if __name__ == "__main__":
    # polynome_to_file_write(5)
    # a = fill_mass_int(15, 1, 4)
    # print(a)
    # print(non_repeating_el(a))
    # print(simple_factor(40))
    # print(pi_with_precision())
    sum_poly('poly1.txt', 'poly2.txt')