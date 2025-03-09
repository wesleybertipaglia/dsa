from collections import deque, Counter

# Not Pythonic
def check_inclusion(s1, s2):
    k = len(s1)
    
    for i in range(len(s2) - k + 1):
        window = s2[i:i + k]
        if sorted(window) == sorted(s1):
            return True
    
    return False

# Pythonic
def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    target = Counter(s1)
    window = Counter()
    k = len(s1)
    
    for i in range(len(s2)):
        window[s2[i]] += 1
        
        # Slide the window when it exceeds size k
        if i >= k:
            window[s2[i - k]] -= 1
            if window[s2[i - k]] == 0:
                del window[s2[i - k]]
        
        if window == target:
            return True
    
    return False