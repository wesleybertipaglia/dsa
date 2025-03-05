'''
Find the max element of an array, but using Divide and Conquer
'''

def max_array(arr, max_num = 0):
    if (max_num < arr[0]):
        max_num = arr[0]
    if (len(arr) == 1):
        return max_num    
    return max_array(arr[1:], max_num)

def test():
    arr1 = [14, 9, 3, 12, 5, 18, 7, 17, 2, 15, 20, 6, 13, 1, 4, 16, 8, 10, 19, 11]
    print(max_array(arr1))

    arr2 = [8, -7, 3, -1, 10, 6, -3, 0, -6, 2, -8, 5, -2, 4, -10, 7, -4, -9, 9, 1, -5]
    print(max_array(arr2))

    arr3 = [9, 8, 6, 3, 65, 3, 9, -1, 2, 10, 36, 918, 93, 63, 51, 12, 5, 1, 7, 14]
    print(max_array(arr3))

test()