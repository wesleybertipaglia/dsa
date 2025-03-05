def binary_search(arr, target):
    low_idx = 0
    high_idx = len(arr) - 1

    while (low_idx <= high_idx):
        mid_idx = (low_idx + high_idx) // 2

        if (arr[mid_idx] == target):
            return mid_idx
        elif (arr[mid_idx] < target):
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1

    return -1

def test():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(binary_search(arr1, 16))

    arr2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr2, -7))

    arr3 = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 36, 51, 63, 65, 93, 918]
    print(binary_search(arr3, 918))

test()