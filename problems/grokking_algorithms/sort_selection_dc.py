def find_smallest(arr):
    smallest_idx = 0

    for i in range (1,len(arr)):
        if (arr[i] < arr[smallest_idx]):
            smallest_idx = i
    
    return smallest_idx

def selection_sort(arr):
    new_arr = []

    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    
    return new_arr

def test():
    arr1 = [14, 9, 3, 12, 5, 18, 7, 17, 2, 15, 20, 6, 13, 1, 4, 16, 8, 10, 19, 11]
    print(selection_sort(arr1))

    arr2 = [8, -7, 3, -1, 10, 6, -3, 0, -6, 2, -8, 5, -2, 4, -10, 7, -4, -9, 9, 1, -5]
    print(selection_sort(arr2))

    arr3 = [9, 8, 6, 3, 65, 3, 9, -1, 2, 10, 36, 918, 93, 63, 51, 12, 5, 1, 7, 14]
    print(selection_sort(arr3))

test()