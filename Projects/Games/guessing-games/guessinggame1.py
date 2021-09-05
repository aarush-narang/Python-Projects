import random

try:
    user_random_number_limit = int(input('What number would you like to guess between? (1-your choice) '))
    if user_random_number_limit < 2:
        print('That number is too low!')
        exit(0)
    elif user_random_number_limit < 10:
        print('That would be too easy!')
        exit(0)
except ValueError:
    print('Please enter an integer')
    exit(0)

random_number = random.randint(1, user_random_number_limit)

user_guess = 0
tries = 0

while user_guess != random_number:
    try:
        new_guess = int(input(f'Guess a number between 1 and {user_random_number_limit} '))
        if new_guess > user_random_number_limit:
            print(f'Guess is over {user_random_number_limit}')
            continue
        elif new_guess < 1:
            print('Guess is less than 1')
            continue
        elif new_guess == user_guess:
            print('You just guessed that!')
            continue

        user_guess = new_guess
        tries += 1
        if user_guess == random_number:
            print(f'You got the number in {tries} tries!')
            exit(0)
        else:
            if user_guess > random_number:
                print(f'The number is lower than {user_guess}')
            elif user_guess < random_number:
                print(f'The number is greater than {user_guess}')
    except ValueError:
        print('Please enter an integer')
