'''
Sum all elements of an array, but using Divide and Conquer
'''

def sum_array(arr):
    if (len(arr) == 1):
        return arr[0]
    return arr[0] + sum_array(arr[1:])

def test():
    arr1 = [14, 9, 3, 12, 5, 18, 7, 17, 2, 15, 20, 6, 13, 1, 4, 16, 8, 10, 19, 11]
    print(sum_array(arr1))

    arr2 = [8, -7, 3, -1, 10, 6, -3, 0, -6, 2, -8, 5, -2, 4, -10, 7, -4, -9, 9, 1, -5]
    print(sum_array(arr2))

    arr3 = [9, 8, 6, 3, 65, 3, 9, -1, 2, 10, 36, 918, 93, 63, 51, 12, 5, 1, 7, 14]
    print(sum_array(arr3))

test()