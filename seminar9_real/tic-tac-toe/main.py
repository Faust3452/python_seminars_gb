import emoji
import math


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
            field[move] = emoji.emojize(":x:", language='alias')
            show_field(field)
            if check_win(field, emoji.emojize(":x:", language='alias')):
                winner = who
                ind = False
        else:
            field[move] = emoji.emojize(":o:", language='alias')
            show_field(field)
            if check_win(field, emoji.emojize(":o:", language='alias')):
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


if __name__ == "__main__":
    cross_zero()
