from collections import defaultdict

# Not Pythonic
def group_anagrams(strs):
    result = []
    
    while strs:
        base = strs.pop()
        anagrams = [base]
        
        for s in strs[:]:
            if sorted(s) == sorted(base):
                anagrams.append(s)
                strs.remove(s)
        
        result.append(anagrams)
    
    return result

# Pythonic
def group_anagrams(strs):
    anagram_map = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)
    
    return list(anagram_map.values())
