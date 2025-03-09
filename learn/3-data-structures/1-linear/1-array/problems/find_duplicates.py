# Not Pythonic
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        if arr[i] not in arr[:i] and arr.count(arr[i]) > 1:
            duplicates.append(arr[i])
    return duplicates

# Pythonic
def find_duplicates_pythonic(arr):
    return list(set([x for x in arr if arr.count(x) > 1]))
