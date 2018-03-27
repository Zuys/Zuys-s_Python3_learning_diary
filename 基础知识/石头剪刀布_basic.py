import random
guess_list = ['石头','剪刀','布']
win_combination = [["布","石头"],["石头","剪刀"],['剪刀','布']]

while True:
    computer = random.choice(guess_list)
    people = input("Please input:  ")

    if people not in guess_list:
        continue
    elif computer == people:
        print("Fight Again!!")
        continue
    elif [computer, people] in win_combination:
        print("Computer wins!!!")
    else:
        print("Human wins!!!")
    break
