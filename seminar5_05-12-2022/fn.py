import math, random


def file_change(filename, remove='абв'):
    f = open(filename, mode='r', encoding='utf-8')
    str = f.read()
    replace_index_list = []
    remove_words_list = []
    print(f'String is \n{str}')
    ind = 0
    start = 0
    while ind != -1:
        ind = str[start:].find(remove)
        start = start + ind + 1
        if ind != -1:
            replace_index_list.append(start-1)
    print(replace_index_list)
    for i in replace_index_list:
        print(f'current ind = {i}')
        left_side = ''
        right_side = ''
        if str[i-1].isalpha() and i != 0:
            j = 1
            while str[i-j].isalpha() and i-j != -1:
                left_side += str[i-j]
                j += 1
            left_side = left_side[::-1]
        if str[i+1].isalpha():
            j = 0
            ind = True
            while ind:
                if str[i+j].isalpha():
                    right_side += str[i+j]
                else:
                    ind = False
                j += 1
                if i+j == len(str):
                    ind = False
        word = left_side + right_side
        if word == '':
            word = remove
        remove_words_list.append(word)
    remove_words_list = set(remove_words_list)
    remove_words_list = list(remove_words_list)
    if remove in remove_words_list:
        ind = 1
        remove_words_list.remove(remove)
    for i in range(len(remove_words_list)):
        str = str.replace(remove_words_list[i], '')
    if ind == 1:
        str = str.replace(remove, '')
    print(f'Changed string is \n{str}')
    f = open(filename, mode='w', encoding='utf-8')
    f.write(str)
    f.close()


def check_win(field, player):
    if field[0] == player and field[1] == player and field[2] == player:
        return True
    elif field[3] == player and field[4] == player and field[5] == player:
        return True
    elif field[6] == player and field[7] == player and field[8] == player:
        return True
    elif field[0] == player and field[3] == player and field[6] == player:
        return True
    elif field[1] == player and field[4] == player and field[7] == player:
        return True
    elif field[2] == player and field[5] == player and field[8] == player:
        return True
    elif field[0] == player and field[4] == player and field[8] == player:
        return True
    elif field[2] == player and field[4] == player and field[6] == player:
        return True
    else:
        return False


def show_field(field):
    print(f'{field[0]} | {field[1]} | {field[2]} ')
    print('---------')
    print(f'{field[3]} | {field[4]} | {field[5]} ')
    print('---------')
    print(f'{field[6]} | {field[7]} | {field[8]} ')
    print('---------')


def cross_zero():
    field = [x for x in range(9)]
    show_field(field)
    ind = True
    move = math.inf
    who = 0
    cnt = 0
    winner = math.inf
    occupied_positions = []
    while ind:
        while move not in list(range(9)):
            move = int(input(f'Ходит игрок №{who+1}. Введите желаемый ход:'))
            if move not in field:
                print('Данная позиция уже занята! Повторите ввод!')
                move = math.inf
        if who == 0:
            field[move] = 'x'
            show_field(field)
            if check_win(field, 'x') == True:
                winner = who
                ind = False
        else:
            field[move] = 'y'
            show_field(field)
            if check_win(field, 'y') == True:
                winner = who
                ind = False

        if ind and who == 0:
            who = 1
        else:
            if ind:
                who = 0
        move = math.inf
        for i in range(len(field)):
            if str(type(field[i])) == "<'class str'>" and i not in occupied_positions:
                occupied_positions.append(i)
                cnt += 1
        if cnt == 9:
            ind = False
    if winner == math.inf:
        print('Ничья!')
    else:
        print(f'Победил игрок №{who+1}')


def rle(filename, mode='compress', filename_out='out.txt'):
    f = open(filename, mode='r', encoding='utf-8')
    f_str = f.read()
    if mode == 'compress':
        print(f'string for compressing: {f_str}')
        new_str = ''
        cnt = 0
        for i in range(len(f_str)):
            if i < len(f_str) - 1:
                if f_str[i] == f_str[i+1]:
                    cnt += 1
                else:
                    cnt += 1
                    new_str += str(cnt) + f_str[i]
                    cnt = 0
            else:
                if f_str[i-1] == f_str[i]:
                    cnt += 1
                    new_str += str(cnt) + f_str[i]
                else:
                    new_str += str(1) + f_str[i]
        print(f'compressed string: {new_str}')

    if mode == 'decompress':
        print(f'string for decompressing: {f_str}')
        new_str = ''
        for i in list(range(len(f_str)))[::2]:
            new_str += int(f_str[i]) * f_str[i+1]
        print(f'decompressed string: {new_str}')

    f = open(filename_out, mode='w', encoding='utf-8')
    f.write(new_str)
    f.close()


def growing_series(s_list: list):
    series_res = []
    for i in range(len(s_list)):
        tmp_list = []
        tmp = s_list[i]
        for j in range(i+1, len(s_list)):
            ind = True
            k = j
            tmp_list.append(s_list[i])
            while ind:
                if k != len(s_list) - 1:
                    if tmp < s_list[k]:
                        tmp_list.append(s_list[k])
                        tmp = s_list[k]
                    k += 1
                else:
                    if k == len(s_list) - 1:
                        if tmp < s_list[k]:
                            tmp_list.append(s_list[k])
                    series_res.append(tmp_list)
                    tmp_list = []
                    tmp = s_list[i]
                    ind = False
    for i in series_res:
        if len(i) <= 1:
            series_res.remove(i)

    for i in range(len(series_res)):
        for j in range(i+1, len(series_res) - 1):
            if series_res[i] == series_res[j]:
                series_res.remove(series_res[i])

    for i in series_res:
        if len(i) > 2:
            for j in range(1, len(i)):
                if len(i[:j]) > 1:
                    series_res.append(i[:j])
    print(f'{s_list} -> {series_res}')


def candies_player_vs_player():
    candies = 2021
    player = random.randint(0, 1)
    print(f'Жеребьевка проведена, первым ходит игрок №{player+1}')
    while candies != 0:
        if candies <= 28:
            print(f'Осталось {candies} конфет! Игрок №{player+1} забирает их за один ход!\nИгрок {player+1} ПОБЕЖДАЕТ!!!')
            candies = 0
        else:
            move = math.inf
            while move not in list(range(1, 29)):
                move = int(input(f'Ходит игрок №{player+1}. Введите количество конфет (от 1 до 28), чтобы забрать: '))
                if move not in list(range(1, 29)):
                    print('Вы ввели неверное количество конфет, повторите ввод!!!')
            candies -= move
            print(f'Игрок №{player+1} забирает {move} конфет! Осталось {candies} конфет!\n')
            if player == 0:
                player = 1
            else:
                player = 0


def candies_bot_vs_player():
    print('Добро пожаловать в игру против бота!')
    candies = 2021
    player = random.randint(0, 1)
    if player == 0:
        p = 'игрок'
    else:
        p = 'бот'
    print(f'Жеребьевка проведена, первым ходит {p}')
    while candies != 0:
        if candies <= 28:
            if player == 0:
                print(f'Осталось {candies} конфет! Игрок забирает их за один ход!\nИгрок ПОБЕЖДАЕТ!!!')
                candies = 0
            else:
                print(f'Осталось {candies} конфет! Бот забирает их за один ход!\nБот ПОБЕЖДАЕТ!!!')
        else:
            move = math.inf
            if player == 0:
                while move not in list(range(1, 29)):
                    move = int(input(f'Ходит игрок! Введите количество конфет (от 1 до 28), чтобы забрать: '))
                    if move not in list(range(1, 29)):
                        print('Вы ввели неверное количество конфет! ')
                candies -= move
                print(f'Игрок забирает {move} конфет! Осталось {candies} конфет!\n')
            else:
                print('Ходит бот!')
                move = random.randint(1, 29)
                candies -= move
                print(f'Бот забирает {move} конфет! Осталось {candies} конфет!\n')
            if player == 0:
                player = 1
            else:
                player = 0


def candies_clever_bot_vs_player():
    print('Добро пожаловать в игру против бота!')
    candies = 2021
    player = random.randint(0, 1)
    if player == 0:
        p = 'игрок'
    else:
        p = 'бот'
    print(f'Жеребьевка проведена, первым ходит {p}')
    while candies != 0:
        if candies <= 28:
            if player == 0:
                print(f'Осталось {candies} конфет! Игрок забирает их за один ход!\nИгрок ПОБЕЖДАЕТ!!!')
                candies = 0
            else:
                print(f'Осталось {candies} конфет! Бот забирает их за один ход!\nБот ПОБЕЖДАЕТ!!!')
                candies = 0
        else:
            move = math.inf
            if player == 0:
                while move not in list(range(1, 29)):
                    move = int(input(f'Ходит игрок! Введите количество конфет (от 1 до 28), чтобы забрать: '))
                    if move not in list(range(1, 29)):
                        print('Вы ввели неверное количество конфет! ')
                candies -= move
                print(f'Игрок забирает {move} конфет! Осталось {candies} конфет!\n')
            else:
                print('Ходит бот!')
                move = random.randint(1, 29)
                tmp = candies
                while tmp-move < 29 and tmp > 28:
                    move = random.randint(1, 29)
                candies -= move
                print(f'Бот забирает {move} конфет! Осталось {candies} конфет!\n')
            if player == 0:
                player = 1
            else:
                player = 0


if __name__ == '__main__':
    # file_change('text.txt')
    # cross_zero()
    # rle('for_compress.txt', mode='compress')
    # growing_series([1, 5, 7])
    # candies_clever_bot_vs_player()
    pass