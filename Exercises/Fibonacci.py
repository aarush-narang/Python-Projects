from functools import cache
import time

@cache # holy shit this thing makes it fast
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

numbers = []
previousnumber = 0

try:
    numberofnumbers = int(input('How many numbers of the fibonacci sequence would like me to generate? '))
except ValueError:
    print('Please enter an integer')
    exit(0)

start = time.time()

if numberofnumbers < 0:
    print('Please enter an integer greater than or equal to 0')
else:
    numbers = []
    for x in range(numberofnumbers):
        numbers.append(fib(x))

print(numbers)
end = time.time()
print(f'\n{end-start} sec')