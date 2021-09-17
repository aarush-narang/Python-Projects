a = [
    [1, 2, 3],
    [11, 12, 13, 1]

]


def findHorizontalSums(arr):
    sums = {}
    for i in range(len(arr)):  # rows
        r = sum(arr[i])  # sum of each row
        sums[f'r{i}'] = r  # add to dict
    return sums


def findVerticalSums(arr):  # add a way to add columns that are of different sizes (ex: in a 2-row matrix the first row is 3 col wide while the second row is 4 col wide, find the sum of the 3 cil and the fourth
    sums = {}
    for i in range(len(arr[0])):  # columns
        col = 0  # sum of column count
        for j in range(len(arr)):  # rows
            col += arr[j][i]  # add each number in each column to var
        sums[f'c{i+1}'] = col  # add to dict
    return sums


if __name__ == '__main__':
    print(findVerticalSums(a))
