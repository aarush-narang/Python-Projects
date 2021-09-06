def main():
    try:
        year = int(input('Enter a year to check: '))
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            print(f'The year {year} is a leap year')
            return
        else:
            print(f'The year {year} is not a leap year')
            return
    except ValueError:
        print('Please enter a year.')
        return main()


if __name__ == '__main__':
    main()
