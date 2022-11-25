# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
import random


def list_generate(size, max):
    return [random.randint(-max, max) for i in range(size)]


def list_mixer(mix_list):
    free_index = [i for i in range(len(mix_list))]
    for i in range(len(mix_list)):
        mix_ind = free_index.pop(random.randint(0, len(free_index) - 1))
        tmp = mix_list[i]
        mix_list[i] = mix_list[mix_ind]
        mix_list[mix_ind] = tmp
    return mix_list


a = list_generate(15, 100)
print(f'Сгенерированный список: \n{a}\n')
print(f'Пермешанный список: \n{list_mixer(a)}')