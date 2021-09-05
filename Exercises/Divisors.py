# add try and except for int
num = int(input('Enter a number: '))

numrange = list(range(1, num+1))
divisorlist = []

for i in numrange:
    if num % i == 0:
        divisorlist.append(i)

print(divisorlist)