# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import fn

print('Игра игрок против игрока!')
fn.candies_player_vs_player()
print('Игра игрок против бота!')
fn.candies_bot_vs_player()
print('Игра игрок против бота с "интеллектом"!')
fn.candies_clever_bot_vs_player()