a = [1, 2, 3, 4, 5, 12]
b = [2, 4, 6, 8, 10, 12]
c = [1, 2, 3, 5, 7, 12]

def removeduplicates(arr):
    return list(set(arr))  # convert to set to remove the duplicates and then convert back to list


def findduplicates(arr):
    arr2 = list(arr) # create new array to manipulate (need to keep original)
    duplicates = [] # duplicate numbers will be stored here
    for i in range(0, len(arr)):
        del arr2[arr2.index(arr[i])] # delete the value
        if arr[i] in arr2: # if that value (after being deleted) is still in arr2 (the one being manipulated) then...
            duplicates.append(arr[i]) # append it to duplicates because it is a duplicate
    return removeduplicates(duplicates) # if there are 3 numbers of one number (ex: [1, 2, 3, 3, 3], the number 3) there will be two entries of 3 in 'duplicates', remove the duplicate ones


def common_entries_double(arr1, arr2):
    common_entries = [] # common entries in the arrays will be stored here
    for i in range(0, max(len(arr1), len(arr2))-1):
        for j in range(0, min(len(arr1), len(arr2))-1):
            if arr1[i] == arr2[j]: # if the value from the first array is = to the value from the second array, append it to the array 'common_entries'
                common_entries.append(arr2[j])
    return common_entries


def common_entries_triple(arr1, arr2, arr3):
    common_entries = [] # common entries in the arrays will be stored here
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            for k in range(0, len(arr3)):
                if arr1[i] == arr2[j] == arr3[k]: # if the value from the 1st array is = to the value from the 2nd array and both are equal to the value from the 3rd, append it to the array 'common_entries'
                    common_entries.append(arr3[k])
    return common_entries
