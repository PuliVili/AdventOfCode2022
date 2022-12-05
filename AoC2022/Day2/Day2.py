#!/usr/bin/env python3

path = r"/home/vuhl/Projects/AoC2022/Day2/data.txt"
with open(path) as d:
    data = [line.rstrip('\n') for line in d]
 
'''   
#A = rock, B = paper, C = scissors
#X = rock, Y = paper, Z = scissors
player_wins = ['A Y', 'B Z', 'C X']
bot_wins = ['A Z', 'B X', 'C Y']
ties = ['A X', 'B Y', 'C Z']
score_dict = {'X':1, 'Y':2, 'Z':3}

total_score = 0

for score in data:
    if score in player_wins:
        total_score += 6
        
    if score in ties:
        total_score += 3

    total_score += score_dict.get(score[2])
    
print(total_score)

'''
#A = rock, B = paper, C = scissors
#X = rock, Y = paper, Z = scissors
selection = ""

player_needs_to_win = ['A Z', 'B Z', 'C Z']
bot_needs_to_win = ['A X', 'B X', 'C X']
needs_to_tie = ['A Y', 'B Y', 'C Y']

player_wins = ['A Y', 'B Z', 'C X']
bot_wins = ['A Z', 'B X', 'C Y']
ties = ['A X', 'B Y', 'C Z']

score_dict = {'X':1, 'Y':2, 'Z':3}

'''
The instruction tell whether to pick winning, tieing or losing combination.
If the choice is to lose, pick from bot_wins combinations a selection where bot selection matches to actual selection
Corresponding value for player should be chosen.

If choice is to win, do same but for player wins combinations.
'''

total_score = 0

for order in data:
    if order in player_needs_to_win:
        total_score += 6
        for score in player_wins:
            if score[0] == order[0]:
                selection = score[2]
                
    if order in needs_to_tie:
        total_score += 3
        for score in ties:
            if score[0] == order[0]:
                selection = score[2]
                
    if order in bot_needs_to_win:
        for score in bot_wins:
            if score[0] == order[0]:
                selection = score[2]
                
    total_score += score_dict.get(selection)
    
print(total_score)
