# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""




import random



def digit_check(text: str):
    while True:
        try:
            x = int(input(f'Ход {text} игрока, введите кол-во конфет: '))
            if 29 > x > 0:
                return x
            else:
                print('Можно взять не больше 28 конфет')

        except ValueError:
            print('Вы ввели не целое число')


def game_with_player(amount: int):
    gamer1 = 0
    gamer2 = 0
    while amount > 0:
        step_gamer1 = digit_check("первого")
        amount -= step_gamer1
        gamer1 += step_gamer1
        if amount <= 0:
            print('Первый игрок выйграл!')
        step_gamer2 = digit_check("второго")
        amount -= step_gamer2
        gamer2 += step_gamer2
        if amount <= 0:
            print('Второй игрок выйграл!')
        print(amount, gamer1, gamer2)

def game_with_bot(amount: int):
    gamer = 0
    bot = 0
    while amount > 0:
        step_gamer = digit_check("")
        amount -= step_gamer
        gamer += step_gamer
        if amount <= 0:
            print('Игрок выйграл!')
        print("Ход бота: ", end='')
        step_bot = random.randint(1, 29)
        print(step_bot)
        amount -= step_bot
        bot += step_bot
        if amount <= 0:
            print('Бот игрок выйграл!')
        print(amount, gamer, bot)

amount = 2021

choice = int(input("Введите 1 если хотите играть с игроком, \nвведите 2, если хотите играть с ботом:\n"))
if choice == 1:
    game_with_player(amount)
elif choice == 2:
    game_with_bot(amount)


