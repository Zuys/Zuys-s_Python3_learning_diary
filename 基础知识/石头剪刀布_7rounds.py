import random

guess_list = ['石头','剪刀','布']
win_combination = [["布","石头"],["石头","剪刀"],['剪刀','布']]
game_round = 1
game_score = 0

while (game_round <= 7):
    computer = random.choice(guess_list)
    print("game",game_round," / 7")
    people = input("Please input:  ")

    if people not in guess_list:
        continue
    elif computer == people:
        print("Fight Again!!\n")
        continue
    elif [computer, people] in win_combination:
        print("Computer wins!!!\n")
        game_score = game_score - 1
    else:
        print("Human wins!!!\n")
        game_score = game_score + 1

    game_round = game_round + 1

print("Score: ",game_score)
