from datetime import date

today = date.today()
year = today.year

name = input('What is your name?')
age = int(input('What is your age?'))


print(f'{name}, you will turn 100 years old in {(year-age)+100} if you are {age} years old')