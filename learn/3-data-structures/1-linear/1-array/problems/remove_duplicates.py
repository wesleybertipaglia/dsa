# Not Pythonic
def remove_duplicates(arr):
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result

# Pythonic
def remove_duplicates_pythonic(arr):
    return list(set(arr))
