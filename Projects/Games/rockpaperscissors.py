import random

global computerchoice

userchoice = input('Choose rock paper or scissors: ')

if userchoice.lower() != 'rock' and userchoice.lower() != 'paper' and userchoice.lower() != 'scissors':
    print('Please choose rock paper or scissors')
    exit(0)

difficulty = input('Choose a difficulty ([e]asy, [m]edium, [h]ard, [i]mpossible, or [r]andom): ')


def computerchoice(userWin):
    if userchoice.lower() == 'rock' and userWin:
        return 'scissors'
    elif userchoice.lower() == 'paper' and userWin:
        return 'rock'
    elif userchoice.lower() == 'scissors' and userWin:
        return 'paper'
    elif userchoice.lower() == 'rock' and userWin is False:
        return 'paper'
    elif userchoice.lower() == 'paper' and userWin is False:
        return 'scissors'
    elif userchoice.lower() == 'scissors' and userWin is False:
        return 'rock'


if difficulty == 'easy' or difficulty == 'e':
    if random.randint(1, 100) < 90:
        computerchoice = computerchoice(True)
    else:
        computerchoice = computerchoice(False)
elif difficulty == 'medium' or difficulty == 'm':
    if random.randint(1, 100) < 60:
        computerchoice = computerchoice(True)
    else:
        computerchoice = computerchoice(False)
elif difficulty == 'hard' or difficulty == 'h':
    if random.randint(1, 100) < 10:
        computerchoice = computerchoice(True)
    else:
        computerchoice = computerchoice(False)
elif difficulty == 'impossible' or difficulty == 'i':
    if random.randint(1, 100) < 0:
        computerchoice = computerchoice(True)
    else:
        computerchoice = computerchoice(False)
elif difficulty == 'random' or difficulty == 'r':
    computerchoice = ['rock', 'paper', 'scissors'][random.randrange(-1, 2)]
else:
    print('Please choose one of the difficulties provided.')
    exit(0)

print(f'I chose {computerchoice}')


def winCheck(user, computer):
    if user == computer:
        print('We both chose the same, its a tie.')
    elif user == 'rock':
        if computer == 'paper':
            print('Paper beats rock, I win.')
        else:
            print('Rock beats scissors, you win.')
    elif user == 'paper':
        if computer == 'scissors':
            print('Scissors beats paper, I win.')
        else:
            print('Paper beats rock, you win.')
    elif user == 'scissors':
        if computer == 'rock':
            print('Rock beats scissors, I win.')
        else:
            print('Scissors beats paper, you win.')


winCheck(userchoice, computerchoice)
