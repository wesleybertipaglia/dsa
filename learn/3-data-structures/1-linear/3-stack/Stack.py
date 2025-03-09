class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return not self.stack
