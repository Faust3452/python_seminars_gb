# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiple_result(num):
    result = list()
    for i in range(num):
        if i == 0:
            result.append(i + 1)
        else:
            result.append(result[i - 1] * (i + 1))
    return result


number = input('Введите целое число: ')
number = int(number)
res = multiple_result(number)
print(f' N = {number} -> {res}')