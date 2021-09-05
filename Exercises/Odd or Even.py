try:
    inputnum = int(input('Enter a number to see if it is odd or even: '))
except ValueError:
    print('Please enter a valid number')
    exit(-1)

if inputnum % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

if inputnum % 4 == 0:
    print('Your number is also a multiple of 4')

part2 = input('Would you like to check with your own numbers? ')

if part2.lower() == 'yes' or part2.lower() == 'y':
    try:
        num = int(input('Enter the number that you want to check: '))
        check = int(input('Enter the number that you want to check with: '))

        if num % check == 0:
            print(f'{check} is a multiple of {num}')
        else:
            print(f'{check} is not a multiple of {num}, {num}/{check} has a remainder of {num % check}')
    except ValueError:
        print('Invalid number, exited script')
elif part2.lower() == 'no' or part2.lower() == 'n':
    print('Ok')
else:
    print('Invalid answer, exited script.')
