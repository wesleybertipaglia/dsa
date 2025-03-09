# Not Pythonic
def rotate_array(arr, k):
    for i in range(k):
        last_element = arr.pop()
        arr.insert(0, last_element)
    return arr

# Pythonic
def rotate_array_pythonic(arr, k):
    k = k % len(arr)  # Handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]
