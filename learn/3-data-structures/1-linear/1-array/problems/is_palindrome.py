# Not Pythonic
def is_palindrome(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
    return True

# Pythonic
def is_palindrome_pythonic(arr):
    return arr == arr[::-1]
