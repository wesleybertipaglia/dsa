# Not Pythonic
def first_non_repeating_char(s):
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i+1:]:
            return s[i]
    
    return None

# Pythonic
def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None
