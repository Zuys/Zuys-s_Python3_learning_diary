#guess number game

import random

def guess():
    guessTaken = 0

    myName = input("Hey what's your name?\n")

    number = random.randint(1,100)
    print("Now " + myName + ",guess what I am thinking (guess a number 1--100), you have 7 times chance")

    while(guessTaken <= 7):
        guess = int(input("Take a guess\n"))

        guessTaken = guessTaken + 1

        if guess < number:
            print("Too low\n")
        elif guess > number:
            print("Too high\n")
        else:
            return 1

num = guess()
if num == 1 :
    print("Good job! You right!")
else:
    print("Sorry - -")
