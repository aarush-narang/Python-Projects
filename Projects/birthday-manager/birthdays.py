import json
import re


with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)


def printnames():
    names = []
    if len(birthdays) < 1:
        return 'Nobody, add some birthdays!'
    for name in birthdays:
        names.append(name)
    return '\n'.join(names)


print(f'We know the birthdays of \n{printnames()}')
if printnames() == 'Nobody, add some birthdays!':
    person = input('Whose birthday would you like to add? ')
    birthday = input('What date is their birthday? (Format it in MM/DD/YYYY) ')
    if not re.match('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', birthday):
        print('Please enter the date in the format MM/DD/YYYY.')
        exit(0)
    else:
        birthdays[person] = birthday
        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)
        print('Birthday added! You can check or remove their birthday by running this program again')
        exit(0)

response = input('Would you like to find ([f]ind), add ([a]dd), edit ([e]dit) or remove ([r]emove) someone\'s birthday? ')

if response == 'f' or response == 'find':
    person = input('Whose birthday would you like to find? ')
    if person in birthdays:
        print(f'{person}\'s birthday is {birthdays[person]}')
    else:
        print(f'I could not find "{person}" in your birthdays. Maybe you misspelled it? (this is case sensitive)')
elif response == 'a' or response == 'add':
    person = input('Whose birthday would you like to add? ')
    birthday = input('What date is their birthday? (Format it in MM/DD/YYYY) ')
    if not re.match('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', birthday):
        print('Please enter the date in the format MM/DD/YYYY.')
        exit(0)
    else:
        birthdays[person] = birthday
        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)
        print('Birthday added! You can check, remove, or edit their birthday by running this program again')
        exit(0)
elif response == 'e' or response == 'edit':
    person = input('Whose birthday would you like to edit? ')
    if person not in birthdays:
        print(f'I could not find "{person}" in your birthdays. Maybe you misspelled it? (this is case sensitive)')
        exit(0)
    else:
        date = input('What would you like to change their birthday to? (format in MM/DD/YYYY) ')
        if not re.match('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', date):
            print('Please enter the date in the format MM/DD/YYYY.')
            exit(0)
        else:
            birthdays[person] = date
            with open('birthdays.json', 'w') as f:
                json.dump(birthdays, f)
            print('Birthday edited! You can check or remove their birthday by running this program again')
            exit(0)
elif response == 'r' or response == 'remove':
    person = input('Whose birthday would you like to remove? ')
    if person not in birthdays:
        print(f'I could not find "{person}" in your birthdays. Maybe you misspelled it? (this is case sensitive)')
    else:
        del birthdays[person]
        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)
        print('Birthday removed! You can check your birthdays by running this program again')
        exit(0)
else:
    print('Please type either [f]ind, [a]dd, [e]dit, or [r]emove')
    exit(0)
