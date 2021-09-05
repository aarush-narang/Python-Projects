def sigfigcalc(num):
    if isinstance(num, int):
        num_list = list(int(x) for x in str(num))
        for i in range(0, 2):
            x = 0
            while True:
                if num_list[x] != 0:
                    x += 1
                    break
                else:
                    del num_list[x]
            num_list.reverse()
        return len(''.join([str(s) for s in num_list]))
    elif isinstance(num, str):
        num_str = list(num)
        if num_str.index('.') + 1 == len(num_str):
            del num_str[-1]
            return len(num_str)
        else:
            del num_str[num_str.index('.')]
            count = len(num_str)
            for x in num_str:
                if x == '0':
                    count -= 1
                else:
                    break
            return count


def main():
    try:
        num_in = input('Enter a number (decimal or otherwise) to calculate the number of significant figures it has: ')
        if '.' not in list(num_in):
            num_in = int(num_in)
        sigfigs = sigfigcalc(num_in)
        print(f'Your number has {sigfigs} significant figures.')
    except ValueError:
        print('Please enter an integer')
        return main()


if __name__ == '__main__':
    main()
