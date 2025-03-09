# Not Pythonic
def reverse_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Pythonic
def reverse_array_pythonic(arr):
    return arr[::-1]
