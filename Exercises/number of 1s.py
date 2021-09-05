# https://www.reddit.com/r/dailyprogrammer/comments/neg49j/20210517_challenge_390_difficult_number_of_1s/

# 1-100 (incl) = 21
#
import time


def f(number, search_num=1):
    number_count = 0
    for i in range(1, number + 1):
        current_num_list = [int(x) for x in str(i)]
        for j in current_num_list:
            if j == search_num:
                number_count += 1
    return number_count


assert f(1) == 1
assert f(5) == 1
assert f(10) == 2
assert f(20) == 12
assert f(1234) == 689
assert f(5123) == 2557
assert f(70000) == 38000
assert f(123321) == 93395
# assert f(3 ** 35) == 90051450678399649

if __name__ == '__main__':
    try:
        num = int(input('enter a number: '))
        search = int(input('what integer would you like to search for? (0-9): '))
        if search < 0 or search > 9:
            print('Please enter an integer between 0-9')
            exit(0)
        start_time = time.time()
        res = f(num, search)
        print(f'Your number {search} was used {res} time(s) in between 1 and {num} inclusive! ({((time.time() - start_time) * 1000)}ms)')
    except ValueError:
        print('Please enter an integer')
