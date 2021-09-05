normal_numerals = {
    ''
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
subtractive_numerals = {
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4,
}
# if the length of the string is longer than 3 and the subtractive numeral is led by a normal numeral, give an error because not valid roman numeral


def findnumber(numeral):
    if numeral[-2:] in subtractive_numerals:
        sub_numeral = subtractive_numerals[numeral[-2:]]
        rnum1_normal_sum = sum([normal_numerals[x] for x in numeral[:-2]])
        rnum1_sum = sub_numeral + rnum1_normal_sum
    else:
        rnum1_sum = sum([normal_numerals[x] for x in numeral])
    return rnum1_sum


def numcompare(rnum1, rnum2):
    result = findnumber(rnum1) < findnumber(rnum2)
    if result:
        print('The first number you entered is less than the second one')
    else:
        print('The first number you entered is greater than the second one')


rnum1_input = input('Enter the first roman numeral in descending order with subtractive numerals at the end (ex: XXVI = 26 or XXIX = 29): ')
rnum2_input = input('Enter the second roman numeral in descending order with subtractive numerals at the end (ex: XXVI = 26 or XXIX = 29): ')

numcompare(rnum1_input, rnum2_input)
