from collections import deque

# Not Pythonic
def max_sliding_window(nums, k):
    result = []
    
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        result.append(max(window))
    
    return result

# Pythonic
def max_sliding_window(nums, k):
    if not nums:
        return []
    
    result = []
    dq = deque()  # Stores indices of the elements in the current window
    
    for i in range(len(nums)):
        # Remove elements out of this window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove all elements smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # The maximum element in the window is at the front of the deque
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result