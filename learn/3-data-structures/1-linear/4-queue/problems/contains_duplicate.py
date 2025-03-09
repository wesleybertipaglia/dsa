from collections import deque

# Not Pythonic
def contains_duplicate(nums, k):
    window = []
    
    for i in range(len(nums)):
        if i > k:
            window.pop(0)
        
        if nums[i] in window:
            return True
        
        window.append(nums[i])
    
    return False

# Pythonic
def contains_duplicate(nums, k):
    window = set()
    q = deque()
    
    for i in range(len(nums)):
        # Slide the window
        if i > k:
            removed = q.popleft()
            window.remove(removed)
        
        # Check for duplicates
        if nums[i] in window:
            return True
        window.add(nums[i])
        q.append(nums[i])
    
    return False
