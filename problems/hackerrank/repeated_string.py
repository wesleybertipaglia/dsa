# platform: HackerRank
# kit: Interview Preparation Kit
# title: Repeated String
# url: https://www.hackerrank.com/challenges/repeated-string/

# description:
# There is a string, s, of lowercase English letters that is repeated infinitely many times. 
# Given an integer, n, find and print the number of letter a's in the first  letters of the infinite string.

def repeated_string(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)    
    remainder = n % len(s)    
    
    total_a_full_repeats = full_repeats * count_a_in_s
    count_a_in_remainder = s[:remainder].count('a')    
    return total_a_full_repeats + count_a_in_remainder