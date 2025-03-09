# Not Pythonic
def subarray_sum(nums, k):
    count = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if sum(nums[i:j]) == k:
                count += 1
    
    return count

# Pythonic
def subarray_sum(nums, k):
    sum_map = {0: 1}
    total, count = 0, 0
    
    for num in nums:
        total += num
        if total - k in sum_map:
            count += sum_map[total - k]
        sum_map[total] = sum_map.get(total, 0) + 1
    
    return count
