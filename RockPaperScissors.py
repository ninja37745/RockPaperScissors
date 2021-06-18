# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:13:34 2021

@author: ninja
"""
import random
import os
import sys

rock = '1'
paper = '2'
scissors = '3'
stop = '4'

computer_points = 0
player_points = 0

best_of_3_mode = '1'
infinate_mode = '2'

best_of_3_mode_games = 3


mode_choice = input('Chose your mode... 1.Best of 3 or 2.Infinate --> ')

if mode_choice == best_of_3_mode:

    while best_of_3_mode_games > 0:
        
        random_choice = str(random.randint(1, 3))
        
       
        player_choice = input('1.Rock, 2.Paper, 3.Scissors... or 4 to quit --> ')
        
        if player_choice in (rock, paper, scissors, stop):
            if best_of_3_mode_games <= 0:
                if computer_points < player_points:
                    print('You won Congrats!')
                elif computer_points > player_points:
                    print('You lost.')
            elif best_of_3_mode_games > 0:
                if random_choice == player_choice == rock:
                    print('Tie!')
                elif random_choice == player_choice == paper:
                    print('Tie!')
                elif random_choice == player_choice == scissors:
                    print('Tie!')
                elif random_choice == rock and player_choice == scissors:
                    print('You Loose!')
                    computer_points += 1
                    best_of_3_mode_games -= 1
                elif random_choice == rock and player_choice == paper:
                    print('You Win!')
                    player_points += 1
                    best_of_3_mode_games -= 1
                elif random_choice == paper and player_choice == rock:
                    print('You Loose!')
                    computer_points += 1
                    best_of_3_mode_games -= 1
                elif random_choice == paper and player_choice == scissors:
                    print('You Win!')
                    player_points += 1
                    best_of_3_mode_games -= 1
                elif random_choice == scissors and player_choice == rock:
                    print('You Win!')
                    player_points += 1
                    best_of_3_mode_games -= 1
                elif random_choice == scissors and player_choice == paper:
                    print('You Loose!')
                    computer_points += 1
                    best_of_3_mode_games -= 1
                elif player_choice == stop:
                    print('Thanks for playing! See you soon!')
                    break
                print(f'''Your score: {player_points}
computer score: {computer_points}''')
        else:
            print('Hmmmm... Someting isnt quit right try writing 1 for Rock 2 for Paper and 3 for Scissors or 4 to quit')
    print('Thanks for playing! See you soon!')
elif mode_choice == infinate_mode:
    while True:
        
        random_choice = str(random.randint(1, 3))
        
        player_choice = input('1.Rock, 2.Paper, 3.Scissors... or 4 to quit --> ')
        
        if player_choice in (rock, paper, scissors, stop):
            if random_choice == player_choice == rock:
                print('Tie!')
            elif random_choice == player_choice == paper:
                print('Tie!')
            elif random_choice == player_choice == scissors:
                print('Tie!')
            elif random_choice == rock and player_choice == scissors:
                print('You Loose!')
                computer_points += 1
            elif random_choice == rock and player_choice == paper:
                print('You Win!')
                player_points += 1
            elif random_choice == paper and player_choice == rock:
                print('You Loose!')
                computer_points += 1
            elif random_choice == paper and player_choice == scissors:
                print('You Win!')
                player_points += 1
            elif random_choice == scissors and player_choice == rock:
                print('You Win!')
                player_points += 1
            elif random_choice == scissors and player_choice == paper:
                print('You Loose!')
                computer_points += 1
            elif player_choice == stop:
                print('Thanks for playing! See you soon!')
                break
            print(f'''Your score: {player_points}
computer score: {computer_points}''')
        else:
            print('Hmmmm... Someting isnt quit right try writing 1 for Rock 2 for Paper and 3 for Scissors or 4 to quit')
print('Press any key to exit')
os.system('pause > nul')
sys.exit()
    