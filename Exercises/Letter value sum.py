string = input('Enter a string to find the value of it (a=1, ab=3, etc.): ')

letter_values = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}


def letter_sum(string):
    list_string = list(string)
    sum_value = 0
    for i in list_string:
        sum_value += letter_values[list_string[list_string.index(i)]]
    return sum_value


print(letter_sum(string))
