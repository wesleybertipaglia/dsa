# Not Pythonic
def length_of_longest_substring(s):
    max_length = 0
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))
    
    return max_length

# Pythonic
def length_of_longest_substring(s):
    char_map = {}
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        
        char_map[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length
