# Not Pythonic
def sort_stack(stack):
    sorted_stack = []
    while stack:
        temp = stack.pop()
        while sorted_stack and sorted_stack[-1] > temp:
            stack.append(sorted_stack.pop())
        sorted_stack.append(temp)
    while sorted_stack:
        stack.append(sorted_stack.pop())

# Pythonic
def sort_stack_pythonic(stack):
    sorted_stack = []
    while stack:
        temp = stack.pop()
        while sorted_stack and sorted_stack[-1] > temp:
            stack.append(sorted_stack.pop())
        sorted_stack.append(temp)
    stack.extend(reversed(sorted_stack))
