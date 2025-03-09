# Not Pythonic
def intersection(arr1, arr2):
    result = []
    for item in arr1:
        if item in arr2 and item not in result:
            result.append(item)
    return result

# Pythonic
def intersection_pythonic(arr1, arr2):
    return list(set(arr1) & set(arr2))
