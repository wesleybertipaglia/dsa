# Not Pythonic
def pairwise_sum(arr):
    result = []
    for i in range(len(arr) - 1):
        result.append(arr[i] + arr[i + 1])
    return result

# Pythonic
def pairwise_sum_pythonic(arr):
    return [arr[i] + arr[i+1] for i in range(len(arr) - 1)]
