# Создайте программу для игры в ""Крестики-нолики"".


import random
import time
from tkinter import *


def stop_game():
    global game_left
    for i in game_left:
        btn[i].config(state='disabled')

def win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (game[6] == n and game[7] == n and game[8] == n) \
        or (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8] == n) \
            or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True


def push(b):
    global game
    global game_left
    global turn
    global lbl
    game[b] = 'X'
    btn[b].config(text='X', bg='yellow', state='disabled')
    game_left.remove(b)
    if b == 4 and turn == 0:
        r = random.choice(game_left)
    elif b != 4 and turn == 0:
        r = 4
    if turn > 0:
        r = 8 - b
    if r not in game_left:
        try:
            r = random.choice(game_left)
        except IndexError:
            lbl['text'] = 'Игра окончена!'
            stop_game()
    game[r] = 'O'
    time.sleep(0.5)
    btn[r].config(text='O', bg='yellow', state='disabled')
    if win('X'):
        lbl['text'] = 'Вы победили!'
        stop_game()
    elif win('O'): 
        lbl['text'] = 'Вы проиграли!'
        stop_game()
    else:
        if (len(game_left) > 1):
            game_left.remove(r)
        else:
            lbl['text'] = 'Игра окончена!'
            stop_game()
        turn += 1


game = [None] * 9
game_left = list(range(9))
turn = 0

window = Tk()
window.title("Крестики-нолики")
lbl = Label(width=20, text="Крестики-нолики", font=('Arial', 20, 'bold'))
btn = [Button(width=5, height=2, font=('Arial', 28, 'bold'),
              bg='white', command=lambda x=i: push(x)) for i in range(9)]

lbl.grid(row=0, column=0, columnspan=3)
row = 1
col = 0
for i in range(9):
    btn[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

window.mainloop()
