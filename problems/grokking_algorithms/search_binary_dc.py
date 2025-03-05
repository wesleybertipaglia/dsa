'''
Binary search, but using Divide and Conquer
'''

def binary_search(arr, target, start=0, finish=None):
    if (finish is None):
        finish = len(arr) - 1

    if (start > finish):
        return -1
    
    mid = (start + finish) // 2

    if (arr[mid] == target):
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, finish)
    else:
        return binary_search(arr, target, start, mid - 1)


def test():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(binary_search(arr1, 16))

    arr2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr2, -7))

    arr3 = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 36, 51, 63, 65, 93, 918]
    print(binary_search(arr3, 918))

test()