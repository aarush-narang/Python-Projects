import random

class GuessComputerNumber:
    def __init__(self, min=1, max=10, maxguesses=None):
        self.min = min
        self.max = max
        self.maxguesses = maxguesses
        self.tries = 0
        self.number = random.randint(1, max)
        self.old_guess = None
    

    def get_guess(self):
        new_guess = input(f'Guess a number between 1 and {self.max} ')

        if self.validate_guess(new_guess):
            return int(new_guess)
        else:
            return self.get_guess()


    def validate_guess(self, guess):
        try:
            number = int(guess)
            if number > self.max:
                print(f'Guess is over {self.max}')
                return False
            elif number < self.min:
                print(f'Guess is less than {self.min}')
                return False
            elif number == self.old_guess:
                print('You just guessed that!')
                return False
            return True
        except ValueError:
            print('Please enter a valid number')
            return False


    def start_game(self):
        while True:
            if self.tries >= self.maxguesses:
                print(f'The number was {self.number} but you ran out of tries!')
                break
            new_guess = self.get_guess()

            if not self.validate_guess(new_guess):
                continue

            self.old_guess = new_guess
            self.tries += 1

            if new_guess == self.number:
                print(f'You got the number in {self.tries} tries!')
                break
            else:
                if new_guess > self.number:
                    print(f'The number is lower than {new_guess}')
                elif new_guess < self.number:
                    print(f'The number is greater than {new_guess}')


game = GuessComputerNumber(0, 10, 3)
game.start_game()