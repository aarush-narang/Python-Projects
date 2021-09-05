import numpy as np
# https://en.wikipedia.org/wiki/Hungarian_algorithm
# main_list = [[123456789, 752880530, 826085747, 576968456, 721429729], [173957326, 1031077599, 407299684, 67656429, 96549194], [1048156299, 663035648, 604085049, 1017819398, 325233271], [942914780, 664359365, 770319362, 52838563, 720059384], [472459921, 662187582, 163882767, 987977812, 394465693]]
main_list = [[12, 32, 7],  # total:   choose: 12
             [15, 6, 2],   # total:   choose: 2
             [42, 13, 23]]  # total:  choose: 13

# 41
# 27
# 60
# 47
# 55
# 45

#
# 123,456,789   752,880,530   826,085,747  576,968,456   721,429,729  # total: 3,000,821,251  3 | chosen: 123,456,789
# 173,957,326   1,031,077,599 407,299,684  67,656,429    96,549,194   # total: 1,776,540,232  5 | chosen: 96,549,194
# 1,048,156,299 663,035,648   604,085,049  1,017,819,398 325,233,271  # total: 3,658,329,665  1 | chosen: 663,035,648
# 942,914,780   664,359,365   770,319,362  52,838,563    720,059,384  # total: 3,150,491,454  2 | chosen: 52,838,563
# 472,459,921   662,187,582   163,882,767  987,977,812   394,465,693  # total: 2,680,973,775  4 | chosen: 163,882,767
#
#2,760,945,115  3,773,540,724  2,771,672,609  2,703,260,658 2,257,737,271
#     #3             #1             #2             #4            #5


used_columns = []
used_rows = []
total_number = 0
valid_numbers = []


def find_smallest_number(array):
    largest_list_index = None
    largest_list_sum = 0
    # finding the largest row
    for i in range(0, len(array)):
        if type(largest_list_index) is None and i not in used_rows:
            largest_list_index = i
            largest_list_sum = sum(array[i])
        elif sum(array[i]) > largest_list_sum and i not in used_rows:
            largest_list_index = i
            largest_list_sum = sum(array[i])
    used_rows.append(largest_list_index)

    # finding the smallest number in that row
    a = np.array(array[largest_list_index])
    smallest_num = a.min()  # smallest number in the array
    smallest_num_index = a.argmin()  # index of the smallest number
    while smallest_num_index in used_columns:
        a[smallest_num_index] = a.max() + 1
        smallest_num = a.min()  # smallest number in the array
        smallest_num_index = a.argmin()  # index of the smallest number
    used_columns.append(smallest_num_index)  # now this column is used so append the index to used_columns

    return smallest_num


for i in range(0, len(main_list)):
    num = find_smallest_number(main_list)
    total_number += num
    valid_numbers.append(num)

print(total_number, valid_numbers)
