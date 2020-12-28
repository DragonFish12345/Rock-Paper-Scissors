import tkinter as tk
from PIL import Image, ImageTk
import getstats
from random import choice
from abc import abstractmethod
import json

root = abstractmethod(tk.Tk())
root.title('Rock Paper Scissors')
root.geometry('800x500')
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', root.destroy)
root.deiconify()


# Stats
get_wins = getstats.get_wins
get_ties = getstats.get_ties
get_losses = getstats.get_losses

wins = get_wins()
ties = get_ties()
losses = get_losses()

# Title Label
title_label = tk.Label(root, text='Rock Paper Scissors')
title_label.grid(row=0, column=0)

stats_label = tk.Label(root, text=f'Wins: {wins} Ties: {ties} Losses: {losses}')
stats_label.grid(row=0, column=1)

# Button Commands


def restartgame():
    rock_button['state'] ='a'
    paper_button['state'] = 'a'
    scissors_button['state'] = 'a'
    fin = open('stats.json')
    wins, ties, losses = fin.read().splitlines()
    stats_label.config(text=f'Wins: {wins} Ties: {ties} Losses: {losses}')
    stats_label.update()


def game(user_choice):
    rock_button['state'] = 'd'
    paper_button['state'] = 'd'
    scissors_button['state'] = 'd'
    choices = ['rock', 'paper', 'scissors']
    computer_choice = choice(choices)
    result_label = tk.Label(root, text=f'You played {user_choice}. The computer played {computer_choice}')
    result_label.grid(row=2, column=1)
    result = ''
    if user_choice == computer_choice:
        result = 'Tied'

    elif user_choice == 'rock':
        if computer_choice == 'paper':
            result = 'Lost'

        elif computer_choice == 'scissors':
            result = 'Won'

    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            result = 'Lost'

        elif computer_choice == 'rock':
            result = 'Won'

    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            result = 'Lost'

        elif computer_choice == 'paper':
            result = 'Won'

    fin = open('stats.json')
    wins, ties, losses = fin.read().splitlines()
    wins = int(wins)
    ties = int(ties)
    losses = int(losses)
    if result == 'Won':
        wins += 1

    elif result == 'Tied':
        ties += 1

    elif result == 'Lost':
        losses += 1

    fin = open('stats.json', 'w+')
    fin.write(str(wins) + '\n')
    fin.write(str(ties) + '\n')
    fin.write(str(losses) + '\n')

    result_label_2 = tk.Label(root, text=f'You {result}')
    result_label_2.grid(row=3, column=1)

    restart_button = tk.Button(root, text='Restart', command=restartgame)
    restart_button.grid(row=4, column=1)


# Buttons and Images

# Rock
rock_image_before = Image.open('rock.jfif')
rock_image_after = rock_image_before.resize((210, 140))
rock_image = ImageTk.PhotoImage(rock_image_after)
rock_button = tk.Button(root, image=rock_image, command=lambda: game('rock'))
rock_button.grid(row=1, column=0)

# Paper
paper_image_before = Image.open('paper.jfif')
paper_image_after = paper_image_before.resize((210, 140))
paper_image = ImageTk.PhotoImage(paper_image_after)
paper_button = tk.Button(root, image=paper_image, command=lambda: game('paper'))
paper_button.grid(row=1, column=1)

# Scissors
scissors_image_before = Image.open('scissors.jfif')
scissors_image_after = scissors_image_before.resize((210, 140))
scissors_image = ImageTk.PhotoImage(scissors_image_after)
scissors_button = tk.Button(root, image=scissors_image, command=lambda: game('scissors'))
scissors_button.grid(row=1, column=2)


root.mainloop()
