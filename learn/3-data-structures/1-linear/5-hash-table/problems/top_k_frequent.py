from collections import Counter
import heapq

# Not Pythonic
def top_k_frequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]

# Pythonic
def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
