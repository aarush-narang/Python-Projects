import math

numbers = []
previousnumber = 0

try:
    numberofnumbers = int(input('How many numbers of the fibonacci sequence would like me to generate? '))
except ValueError:
    print('Please enter an integer')
    exit(0)


if numberofnumbers < 0:
    print('Please enter an integer greater than or equal to 0')
elif numberofnumbers == 0:
    numbers = []
elif numberofnumbers == 1:
    numbers = [1]
elif numberofnumbers == 2:
    numbers = [1, 1]
elif numberofnumbers > 2:
    numbers = [1, 1]
    for x in range(numberofnumbers-2):
        numbers.append(numbers[x]+numbers[x+1])

str_numbers = [str(int) for int in numbers] # converts ints to strings so it can be joined

print(', '.join(str_numbers))
