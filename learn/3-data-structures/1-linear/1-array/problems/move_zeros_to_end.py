# Not Pythonic
def move_zeros_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
    result = [x for x in arr if x != 0] + [0] * count
    return result

# Pythonic
def move_zeros_to_end_pythonic(arr):
    return [x for x in arr if x != 0] + [0] * arr.count(0)
