# Not Pythonic
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    
    return False

# Pythonic
def contains_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
