from collections import Counter

# Not Pythonic
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

# Pythonic
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
