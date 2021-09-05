inputstringlist = input('Enter a string: ')

if(inputstringlist == inputstringlist[::-1]):
    print('Your string is a palindrome')
else:
    print('Your string is not a palindrome')