'''
Merge sort is a fast sorting algotithm, that use divide and conquer
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def test():
    arr1 = [14, 9, 3, 12, 5, 18, 7, 17, 2, 15, 20, 6, 13, 1, 4, 16, 8, 10, 19, 11]
    print(merge_sort(arr1))

    arr2 = [8, -7, 3, -1, 10, 6, -3, 0, -6, 2, -8, 5, -2, 4, -10, 7, -4, -9, 9, 1, -5]
    print(merge_sort(arr2))

    arr3 = [9, 8, 6, 3, 65, 3, 9, -1, 2, 10, 36, 918, 93, 63, 51, 12, 5, 1, 7, 14]
    print(merge_sort(arr3))

test()