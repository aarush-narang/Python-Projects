coins_usd = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 50, 100]
coins_other = [1, 5, 10, 25, 100, 500]


def change(amount, coins):
    coins.reverse()
    a = dict.fromkeys(coins, 0)
    while amount > 0:
        for i in coins:
            while i <= amount:
                amount -= i
                a[i] += 1
    # total_string = f'Your change is {a[100]} $100 bill(s), {a[50]} $50 bill(s), {a[20]} $20 bill(s), {a[10]} $10 bill(s), {a[5]} $5 bill(s), {a[1]} $1 bill(s), {a[0.25]} 25¢ coins, {a[0.1]} 10¢ coins, {a[0.05]} 5¢ coins, {a[0.01]} 1¢ coins'
    return f'You get a total of {sum(a.values())} coins/bills'


def main():
    try:
        amount_given = int(input('Enter an integer: '))
        print(change(amount_given, coins_usd)) # change currency here!
    except ValueError:
        print('Please enter an integer value. ')
        main()


if __name__ == '__main__':
    main()


