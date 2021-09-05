# https://www.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/

def nonogramrow(arr: list):
    if len(arr) == 0:
        return []
    arr = ''.join([str(x) for x in arr])
    arr = arr.split('0')
    arr_entries_lengths = []
    if len(arr[0]) == 0:
        del arr[0]
    if len(arr[-1]) == 0:
        del arr[-1]
    for i in range(0, len(arr)):
        arr_entries_lengths.append(len(arr[i]))
    arr_entries_lengths = [x for x in arr_entries_lengths if x != 0]
    return arr_entries_lengths


assert nonogramrow([]) == []
assert nonogramrow([0,0,0,0,0]) == []
assert nonogramrow([1,1,1,1,1]) == [5]
assert nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) == [5,4]
assert nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) == [2,1,3]
assert nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) == [2,1,3]
assert nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) == [1,1,1,1,1,1,1,1]


if __name__ == '__main__':
    arr_of_ones_and_zeros = [0,0,0,0,0]
    print(nonogramrow(arr_of_ones_and_zeros))
