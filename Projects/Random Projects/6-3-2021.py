import random

print('I have a ball and it is under one of three cups. Guess a number between 1-3 (1 for the first cup, 2 for the second cup, etc.)')

cup = random.randint(1, 3)

try:
    guess = int(input('Guess a number: '))
except ValueError:
    print('Please enter a number')

if guess > 3:
    print('Please guess a number between 1 and 3')
elif guess != cup:
    print(f'You did not guess the correct cup, the ball was in cup {cup}')
else:
    print('You got the correct cup!')
