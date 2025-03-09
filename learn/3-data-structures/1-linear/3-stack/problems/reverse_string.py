# Not Pythonic
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# Pythonic
def reverse_string_pythonic(s):
    stack = list(s)
    return ''.join(stack[::-1])
