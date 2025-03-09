# Not Pythonic
def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0

# Pythonic
def is_balanced_parentheses_pythonic(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack
