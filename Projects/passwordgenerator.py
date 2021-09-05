# generate multiple passwords and print them
# check for dictionary words

import random


def yesnotruefalse(value):  # converts responses into booleans to make it easier to handle
    if value != 'no' and value != 'n' and value != 'yes' and value != 'y':
        print('Please enter [y]es or [n]o')
        exit(0)
    if value.lower() == 'yes' or value.lower() == 'y':
        return True
    elif value.lower() == 'no' or value.lower() == 'n':
        return False


def generatecharacterset(upper, lower, numbers, symbols):  # takes their responses (as booleans) and generates a character set
    characterset = ''
    uppercaseletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercaseletters = 'abcdefghijklmnopqrstuvwxyz'
    allnumbers = '1234567890'
    allsymbols = '`~!@#$%^&*()_+-=[]{}\\|:;\'",<.>/?'
    if upper:
        characterset += uppercaseletters
    if lower:
        characterset += lowercaseletters
    if numbers:
        characterset += allnumbers
    if symbols:
        characterset += allsymbols
    return characterset


def generatepasswithset(characterset, length):  # generates a password randomly with the character set and password length of their choice
    p = ''
    while len(p) < length:
        p += characterset[random.randint(0, len(characterset) - 1)]
    return p


# defaults
uppercase = True
lowercase = True
symbols = False
numbers = False

# asks for the length
try:
    passlen = int(input('What would you like the length of your password to be? '))
    if passlen < 8:
        choice = yesnotruefalse(input('Are you sure you want to make a password less than 8 characters in length? '))
        if not choice:
            print('Ok, exiting')
            exit(0)
except ValueError:
    print('Please enter an integer')
    exit(0)

uppercase = yesnotruefalse(input('Would you like uppercase characters in your password? ([y]es or [n]o) '))
lowercase = yesnotruefalse(input('Would you like lowercase characters in your password? ([y]es or [n]o) '))
numbers = yesnotruefalse(input('Would you like numbers in your password? ([y]es or [n]o) '))
symbols = yesnotruefalse(input('Would you like symbols in your password? ([y]es or [n]o) '))

# character set
characters = generatecharacterset(uppercase, lowercase, numbers, symbols)
if len(characters) == 0:  # if they say no to every option, nothing will be in the character set, therefore there will be no password generated
    print('Unable to generate a password. There are too few characters in the character set.')
    exit(0)

password = generatepasswithset(characters, passlen)

print(f'Your password is {password}')
