import math
# run a bunch of trials with this algorithm and average the number of tries it takes
# use another algorithm in which it halves it every guess (and truncates if necessary) and run a bunch of trials with that and see the average number of tries


try:
    user_number_limit = int(input('What is your number between? (1 and ___) '))
    user_number = int(input('Please tell me your number so that I can check whether my guess is higher or lower. '))
    if user_number >= user_number_limit:
        print('Your number has to be less than the limit you set.')
        exit(0)
    elif user_number <= 1:
        print('Your number has to be greater than 1')
        exit(0)
except ValueError:
    print('Please enter an integer.')
    exit(0)

guess = 0
tries = 0
upper_limit = user_number_limit
lower_limit = 1

while True:
    tries += 1
    if tries == 1:
        guess = math.floor(user_number_limit / 2)

    if guess > user_number:
        response = True
    elif guess < user_number:
        response = False
    else:
        response = 'win'

    if response == 'win':
        print(f'I got your number ({user_number}) in {tries} trie(s)!')
        exit(0)
    else:
        print(f'Guess: {guess}. Making new guess...')
        if response:
            upper_limit = guess
        else:
            lower_limit = guess

        guess = math.trunc(((upper_limit - lower_limit) / 2) + lower_limit)
