import math


def nextpal(num):
    num_string = str(num)
    length_num = len(num_string)
    half_num_length = math.ceil(length_num / 2)

    front_of_num = num_string[:half_num_length]
    back_of_num = num_string[-half_num_length:]

    if front_of_num[::-1] <= back_of_num:
        front_of_num = str(int(front_of_num) + 1)
    if length_num%2 == 1:
        new_back = front_of_num[:length_num//2][::-1]
    else:
        new_back = front_of_num[::-1]

    return int(f'{front_of_num}{new_back}')


assert nextpal(808) == 818
assert nextpal(999) == 1001
assert nextpal(2133) == 2222
assert nextpal(3**39) == 4052555153515552504

if __name__ == '__main__':
    try:
        print(nextpal(int(input('enter a number: '))))
    except ValueError:
        print('Please enter an integer.')
        print(nextpal(int(input('enter a number: '))))
